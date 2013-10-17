from django.views.generic import ListView, DetailView
from inventory.models import *
from inventory.forms import *


class NodeList(ListView):
    """
    """
    queryset = Node.objects.filter(is_active=True)
    template_name = 'node_list.html'


class NodeDetail(DetailView):
    """
    """
    model = Node
    template_name = 'node_detail.html'


def serialize_sound_layer(sound_queryset=None):
    results = []
    for sound in list(sound_queryset):
        data = sound_to_json(sound)
        results.append(data)

    result_data = {
        'type': 'FeatureCollection',
        'features': results,
    }
    geo_json = mark_safe(json.dumps(result_data))

    return geo_json