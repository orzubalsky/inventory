from django.db.models import *
from django.utils.translation import ugettext_lazy as _
from django.utils import simplejson as json
from django.utils.safestring import mark_safe
from django.db.models.query import QuerySet
from django.contrib.contenttypes.generic import *
from core.models import *
from core.fields import *


class NodeRelationMixin(Model):
    """
    """
    node = OneToOneField("Node")


class NodeArrowSpectrum(ArrowSpectrum, NodeRelationMixin):
    pass


class NodeLineSpectrum(LineSpectrum, NodeRelationMixin):
    pass


class NodeTriangleSpectrum(TriangleSpectrum, NodeRelationMixin):
    pass


class NodeCrossSpectrum(CrossSpectrum, NodeRelationMixin):
    pass


class EdgeRelationMixin(Model):
    """
    """
    edge = ForeignKey("Edge")


class EdgeArrowSpectrum(ArrowSpectrum, EdgeRelationMixin):
    pass


class EdgeLineSpectrum(LineSpectrum, EdgeRelationMixin):
    pass


class EdgeTriangleSpectrum(TriangleSpectrum, EdgeRelationMixin):
    pass


class EdgeCrossSpectrum(CrossSpectrum, EdgeRelationMixin):
    pass


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
                'description': node.description,
                'node_type': node.node_type,
                'highlight': False,
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

    TYPE_CHOICES = (
        ('project', _('Project')),
        ('technology', _('Technology')),
        ('skill', _('Skill')),
        ('concept', _('Concept')),
        ('process', _('Process')),
        ('object', _('Object')),
    )

    name = CharField(max_length=100, blank=True, null=True)
    description = TextField(blank=True, null=True)
    slug = SlugField(max_length=100)
    node_type = CharField(max_length=100, blank=True, null=True, choices=TYPE_CHOICES)
    edges = ManyToManyField("self", through="Edge", symmetrical=False)

    arrows = ManyToManyField(Arrow, through=NodeArrowSpectrum)
    lines = ManyToManyField(Line, through=NodeLineSpectrum)
    triangles = ManyToManyField(Triangle, through=NodeTriangleSpectrum)
    crosses = ManyToManyField(Cross, through=NodeCrossSpectrum)

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

    arrows = ManyToManyField(Arrow, through=EdgeArrowSpectrum)
    lines = ManyToManyField(Line, through=EdgeLineSpectrum)
    triangles = ManyToManyField(Triangle, through=EdgeTriangleSpectrum)
    crosses = ManyToManyField(Cross, through=EdgeCrossSpectrum)

    objects = EdgeManager()

    def __unicode__(self):
        return "%s - %s" % (self.source_node, self.target_node)
