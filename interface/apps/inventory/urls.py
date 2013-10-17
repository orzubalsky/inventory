from django.conf.urls import patterns, url
from inventory.views import *

# orzubalskydotcom application
urlpatterns = patterns('inventory.views',
    url(r'^$', 'node_list', name='node-list'),
)