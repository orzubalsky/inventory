from django.contrib import admin
from inventory.models import *


class BaseAdmin(admin.ModelAdmin):
    """
    """
    pass


class NodeAdmin(BaseAdmin):
    """
    """
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}


# register admin models
admin.site.register(Node)
