from django.db.models import *
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils import simplejson as json
from django.utils.safestring import mark_safe
from django.forms.models import model_to_dict
from django.db.models.query import QuerySet


class Base(Model):
    """
    Base model for all of the models in ff.
    """
    class Meta:
        abstract = True

    created = DateTimeField(
        verbose_name=_("created"),
        editable=False,
        help_text=_("The time when this object was created.")
    )
    updated = DateTimeField(
        verbose_name=_("updated"),
        editable=False,
        help_text=_("The time when this object was edited last.")
    )
    is_active = BooleanField(
        verbose_name=_("is active"),
        default=1,
        help_text=_(
            "This field indicates whether the object is active on the site"
        )
    )

    def save(self, *args, **kwargs):
        """Save timezone-aware values for created and updated fields."""
        if self.pk is None:
            self.created = timezone.now()
        self.updated = timezone.now()
        super(Base, self).save(*args, **kwargs)

    def __unicode__(self):
        if hasattr(self, "name") and self.name:
            return self.name
        else:
            return "%s" % (type(self))


class NodeQuerySet(QuerySet):
    def public(self):
        return self.filter(is_active=True)

    def serialize(self):
        """
        return queryset in arbor.js "branch" format:
        {nodes:{}, edges:{}}
        """
        node_queryset = self.only('name', 'description', 'edges')

        node_dict = {}

        for node in node_queryset:
            node_dict[node.name] = {
                'name': node.name,
                'description': node.description
            }

        edge_queryset = Edge.objects.filter(
            source_node__in=node_queryset, target_node__in=node_queryset).only(
                'source_node',
                'target_node',
                'transaction_type'
            )

        edge_dict = {}

        for edge in edge_queryset:

            model_as_dict = {
                'transaction_type': edge.transaction_type,
            }

            if edge.source_node.name in edge_dict:
             edge_dict[edge.source_node.name][edge.target_node.name] = model_as_dict
            else:
             edge_dict[edge.source_node.name] = {edge.target_node.name: model_as_dict}

        result_data = {
            'nodes': node_dict,
            'edges': edge_dict,
        }
        safe_json = mark_safe(json.dumps(result_data))

        return safe_json


class NodeManager(Manager):
    def get_query_set(self):
        return NodeQuerySet(self.model, using=self._db).prefetch_related(
            'edges__source_node',
            'edges__target_node',
            'edges'
        )

    def public(self):
        return self.get_query_set().public()

    def serialize(self):
        return self.get_query_set().serialize()


class Node(Base):
    """
    """
    class Meta:
        ordering = ['name', ]
        verbose_name_plural = "nodes"

    name = CharField(max_length=100, blank=True, null=True)
    description = TextField(blank=True, null=True)
    slug = SlugField(max_length=100)
    edges = ManyToManyField("self", through="Edge", symmetrical=False)

    objects = NodeManager()

    def get_tags(self):
        return ",".join([tag.name for tag in self.tags.all()])


class EdgeQuerySet(QuerySet):
    def public(self):
        return self.filter(is_active=True)


class EdgeManager(Manager):
    def get_query_set(self):
        return EdgeQuerySet(self.model, using=self._db).select_related(
            'source_node__name',
            'target_node__name',
        )

    def public(self):
        return self.get_query_set().public()

    def serialize(self):
        return self.get_query_set().serialize()


class Edge(Base):
    """
    """
    TRANSACTION_CHOICES = (
        ('gift', _('Gift')),
        ('grant', _('Grant')),
        ('residency', _('Residency')),
        ('installation', _('Installation')),
        ('performance', _('Performance')),
        ('research', _('Research')),
        ('barter', _('Barter')),
        ('paid', _('Paid')),
    )

    source_node = ForeignKey(Node, related_name='source_node')
    target_node = ForeignKey(Node, related_name='target_node')
    transaction_type = CharField(
        max_length=200,
        choices=TRANSACTION_CHOICES,
        blank=True,
        null=True
    )

    objects = EdgeManager()
