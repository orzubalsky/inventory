from django.forms import *
from inventory.models import *
from inventory.widgets import *


class NodeArrowSpectrumForm(forms.ModelForm):
    class Meta:
        model = NodeArrowSpectrum
        fields = ('node', 'relation', 'value_x',)
        widgets = {
            'value_x': SpectrumWidget()
        }


class NodeLineSpectrumForm(forms.ModelForm):
    class Meta:
        model = NodeLineSpectrum
        fields = ('node', 'relation', 'value_x')
        widgets = {
            'value_x': SpectrumWidget()
        }

class NodeCrossSpectrumForm(forms.ModelForm):
    class Meta:
        model = NodeCrossSpectrum
        fields = ('node', 'relation', 'value_x', 'value_y',)
        widgets = {
            'relation': CrossWidget(),
            'value_x': forms.widgets.TextInput(),
            'value_y': forms.widgets.TextInput(),
        }
