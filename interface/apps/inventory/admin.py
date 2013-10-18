from django.contrib import admin
from inventory.models import *


class BaseAdmin(admin.ModelAdmin):
    """
    """
    pass


class SourceEdgeInline(admin.TabularInline):
    model = Edge
    extra = 0
    fields = ('target_node', 'transaction_type')
    fk_name = 'source_node'


class TargetEdgeInline(admin.TabularInline):
    model = Edge
    extra = 0
    fields = ('source_node', 'transaction_type')
    fk_name = 'target_node'


class NodeAdmin(BaseAdmin):
    """
    """
    fields = ('name',)
    list_display = ('name', 'node_type', 'is_active')
    list_editable = ('node_type', 'is_active',)
    #prepopulated_fields = {'slug': ('name',)}
    inlines = (SourceEdgeInline, TargetEdgeInline)


class EdgeAdmin(BaseAdmin):
    """
    """
    list_display = ('source_node', 'target_node', 'transaction_type')
    fields = ('source_node', 'target_node', 'transaction_type')


# register admin models
admin.site.register(Node, NodeAdmin)
admin.site.register(Edge, EdgeAdmin)
