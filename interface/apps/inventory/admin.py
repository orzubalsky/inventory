from django.contrib import admin
from core.admin import *
from inventory.models import *
from inventory.forms import *


class SourceEdgeInline(BaseTabularInline):
    model = Edge
    fields = ('target_node', 'transaction_type')
    fk_name = 'source_node'


class TargetEdgeInline(BaseTabularInline):
    model = Edge
    fields = ('source_node', 'transaction_type')
    fk_name = 'target_node'


class NodeArrowSpectrumInline(BaseTabularInline):
    model = NodeArrowSpectrum
    form = NodeArrowSpectrumForm


class NodeLineSpectrumInline(BaseTabularInline):
    model = NodeLineSpectrum


class NodeTriangleSpectrumInline(BaseTabularInline):
    model = NodeTriangleSpectrum


class NodeCrossSpectrumInline(BaseTabularInline):
    model = NodeCrossSpectrum


class NodeAdmin(BaseAdmin):
    """
    """
    fields = ('name', 'node_type')
    list_display = ('name', 'node_type', 'is_active')
    list_editable = ('node_type', 'is_active',)
    #prepopulated_fields = {'slug': ('name',)}
    inlines = (
        NodeArrowSpectrumInline,
        NodeLineSpectrumInline,
        NodeTriangleSpectrumInline,
        NodeCrossSpectrumInline,
        SourceEdgeInline,
        TargetEdgeInline
    )


class EdgeArrowSpectrumInline(BaseTabularInline):
    model = EdgeArrowSpectrum


class EdgeLineSpectrumInline(BaseTabularInline):
    model = EdgeLineSpectrum


class EdgeTriangleSpectrumInline(BaseTabularInline):
    model = EdgeTriangleSpectrum


class EdgeCrossSpectrumInline(BaseTabularInline):
    model = EdgeCrossSpectrum


class EdgeAdmin(BaseAdmin):
    """
    """
    list_display = ('source_node', 'target_node', 'transaction_type')
    fields = ('source_node', 'target_node', 'transaction_type')
    inlines = (
        EdgeArrowSpectrumInline,
        EdgeLineSpectrumInline,
        EdgeTriangleSpectrumInline,
        EdgeCrossSpectrumInline,
    )


class NodeArrowSpectrumAdmin(BaseAdmin):
    fields = ('node', 'relation', 'value_x')
    form = NodeArrowSpectrumForm


# register admin models
admin.site.register(Node, NodeAdmin)
admin.site.register(Edge, EdgeAdmin)
admin.site.register(NodeArrowSpectrum, NodeArrowSpectrumAdmin)
