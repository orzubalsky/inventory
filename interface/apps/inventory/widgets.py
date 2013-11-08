from django.forms import widgets
from django.conf import settings
from django.template.loader import render_to_string
from core.models import *


class SpectrumWidget(widgets.TextInput):
    class Media:
        css = {
            'all': ('widgets/spectrum/style.css',)
        }
        js = (
            'js/lib/jquery.js',
            'js/lib/jquery-ui.js',
            'widgets/spectrum/Spectrum.js',
            'widgets/spectrum/interaction.js',
        )

    def render(self, name, value, attrs=None):

        params = {
            'field_name': name,
            'value': value,
        }

        return render_to_string('widgets/spectrum.html', params)


class CrossWidget(widgets.Select):
    class Media:
        css = {
            'all': ('widgets/cross/style.css',)
        }
        js = (
            'js/lib/jquery.js',
            'widgets/cross/kinetic.js',
            'widgets/cross/Cross.js',
            'widgets/cross/interaction.js',
        )

    def render(self, name, value, empty_value='', attrs=None, choices=()):

        output = super(CrossWidget, self).render(name, value, attrs, choices)

        try:
            relation = Cross.objects.get(pk=value)
        except Cross.DoesNotExist:
            relation = None

        params = {
            'field': output,
            'relation': relation
        }
        return render_to_string('widgets/cross.html', params)

