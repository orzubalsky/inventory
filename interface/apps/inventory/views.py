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
