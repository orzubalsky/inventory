from django.forms import widgets
from django.conf import settings
from django.template.loader import render_to_string


class ArrowSpectrumWidget(widgets.TextInput):
    class Media:
        css = {
            'all': ('widgets/arrow/style.css',)
        }
        js = (
            'js/lib/jquery.js',
            'js/lib/jquery-ui.js',
            'widgets/arrow/Spectrum.js',
            'widgets/arrow/interaction.js',
        )

    def render(self, name, value, attrs=None):

        params = {
            'field_name': name,
        }

        return render_to_string('widgets/arrow.html', params)
