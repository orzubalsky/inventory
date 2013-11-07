from django.forms import *
from inventory.models import *
from inventory.widgets import *


class NodeArrowSpectrumForm(forms.ModelForm):
    class Meta:
        model = NodeArrowSpectrum
        fields = ('node', 'relation', 'value_x',)
        widgets = {
            'value_x': ArrowSpectrumWidget()
        }
