from django.contrib import admin
from inventory.models import *


class BaseAdmin(admin.ModelAdmin):
    """
    """
    pass


class EdgeInline(admin.TabularInline):
    model = Edge
    extra = 0
    fields = ('target_node', 'transaction_type')
    fk_name = 'source_node'


class NodeAdmin(BaseAdmin):
    """
    """
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = (EdgeInline, )

# register admin models
admin.site.register(Node, NodeAdmin)
