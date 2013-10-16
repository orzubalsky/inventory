from django.conf.urls import patterns, url
from inventory.views import *

# orzubalskydotcom application
urlpatterns = patterns('inventory.views',
    url(r'detail/(?P<slug>[0-9A-Za-z\-]+)$', NodeDetail.as_view(), name='node-detail'),
    url(r'$', NodeList.as_view(template_name="node_list.html"), name='node-list'),
)