from django.shortcuts import render_to_response
from django.template import RequestContext
from inventory.models import *
from inventory.forms import *


def node_list(request):

    branch_json = Node.objects.all().serialize()

    return render_to_response(
        'node_list.html', {
            'branch_json': branch_json,
        }, context_instance=RequestContext(request))
