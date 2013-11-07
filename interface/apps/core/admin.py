from django.contrib import admin
from core.models import *


class BaseAdmin(admin.ModelAdmin):
    """
    """
    pass


class BaseTabularInline(admin.TabularInline):
    """
    """
    extra = 0


class ArrowInline(BaseTabularInline):
    model = Arrow


class LineInline(BaseTabularInline):
    model = Line


class TriangleInline(BaseTabularInline):
    model = Triangle


class CrossInline(BaseTabularInline):
    model = Cross


class TaxonomyAdmin(BaseAdmin):
    fields = ('name', 'is_active')
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)
    inlines = (
        ArrowInline,
        LineInline,
        TriangleInline,
        CrossInline,
    )

admin.site.register(Arrow)
admin.site.register(Line)
admin.site.register(Triangle)
admin.site.register(Cross)
admin.site.register(Taxonomy, TaxonomyAdmin)
