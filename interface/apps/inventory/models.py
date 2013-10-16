from django.db.models import *
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from taggit.managers import TaggableManager


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
            "This field indicates whether the object is active on the "
            "front end of the site. Inactive objects will still be available "
            "through the admin backend."
        )
    )

    def save(self, *args, **kwargs):
        """Save timezone-aware values for created and updated fields."""
        if self.pk is None:
            self.created = timezone.now()
        self.updated = timezone.now()
        super(Base, self).save(*args, **kwargs)

    def __unicode__(self):
        if hasattr(self, "name") and self.title:
            return self.title
        else:
            return "%s" % (type(self))


class Node(Base):
    """
    """
    class Meta:
        verbose_name_plural = "nodes"

    name = CharField(max_length=100, blank=True, null=True)
    description = TextField(blank=True, null=True)
    slug = SlugField(max_length=100)
    related_to = ManyToManyField("self", through="Edge", related_name="related nodes", symmetrical=False)
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.title

    def get_tags(self):
        return ",".join([tag.name for tag in self.tags.all()])


class Edge(Base):
    """
    """
    TRANSACTION_CHOICES = (
        ('gift', _('Gift')),
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
