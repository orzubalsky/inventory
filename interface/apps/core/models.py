from django.db.models import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import *
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils import simplejson as json
from django.utils.safestring import mark_safe
from django.db.models.query import QuerySet


class BaseQuerySet(QuerySet):
    def public(self):
        return self.filter(is_active=True)


class BaseManager(Manager):
    def get_query_set(self):
        return BaseQuerySet(self.model, using=self._db)

    def public(self):
        return self.get_query_set().public()


class Base(Model):
    """
    Base model, adding created and updated datetime metadata,
    saved with timezone aware data.
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

    objects = BaseManager()

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


class Taxonomy(Base):
    class Meta:
        verbose_name_plural = 'taxonomies'

    name = CharField(max_length=100)


class Arrow(Model):
    """
    """
    key_x = CharField(max_length=100)
    taxonomy = ForeignKey(Taxonomy, blank=True, null=True)

    def __unicode__(self):
        return self.key_x


class Line(Model):
    """
    """
    key_x1 = CharField(max_length=100)
    key_x2 = CharField(max_length=100)
    taxonomy = ForeignKey(Taxonomy, blank=True, null=True)

    def __unicode__(self):
        return "%s - %s" % (self.key_x1, self.key_x2)


class Triangle(Model):
    """
    """
    key_x = CharField(max_length=100)
    key_y = CharField(max_length=100)
    key_z = CharField(max_length=100)
    taxonomy = ForeignKey(Taxonomy, blank=True, null=True)

    def __unicode__(self):
        return "%s - %s - %s" % (
            self.key_x,
            self.key_y,
            self.key_z
        )


class Cross(Model):
    """
    """
    key_x1 = CharField(max_length=100)
    key_x2 = CharField(max_length=100)
    key_y1 = CharField(max_length=100)
    key_y2 = CharField(max_length=100)
    taxonomy = ForeignKey(Taxonomy, blank=True, null=True)

    def __unicode__(self):
        return "%s - %s x %s - %s" % (
            self.key_x1,
            self.key_x2,
            self.key_y1,
            self.key_y2,
        )


class Spectrum(Model):
    """
    """
    class Meta:
        abstract = True
        verbose_name_plural = "spectra"

    value_x = DecimalField(max_digits=4, decimal_places=3)

    def __unicode__(self):
        return "%s: %f" % (type(self), self.value)


class ArrowSpectrum(Spectrum):
    """
    """
    class Meta:
        abstract = True
        verbose_name_plural = "arrow spectra"

    relation = ForeignKey(Arrow)

    def __unicode__(self):
        return "%s: %f" % (self.relation, self.value)


class LineSpectrum(Spectrum):
    """
    """
    class Meta:
        abstract = True
        verbose_name_plural = "line spectra"

    relation = ForeignKey(Line)

    def __unicode__(self):
        return "%s: %f" % (self.relation, self.value)


class TriangleSpectrum(Spectrum):
    """
    """
    class Meta:
        abstract = True
        verbose_name_plural = "triangle spectra"

    value_y = DecimalField(max_digits=4, decimal_places=3)
    value_z = DecimalField(max_digits=4, decimal_places=3)
    relation = ForeignKey(Triangle)

    def __unicode__(self):
        return "%s: %f" % (self.relation, self.value)


class CrossSpectrum(Spectrum):
    """
    """
    class Meta:
        abstract = True
        verbose_name_plural = "cross spectra"

    value_y = DecimalField(max_digits=4, decimal_places=3)
    relation = ForeignKey(Cross)

    def __unicode__(self):
        return "%s: %f" % (self.relation, self.value)
