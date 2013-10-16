from django.conf import settings
from inventory.models import *


def google_analytics(request):
    try:
        if settings.GOOGLE_ANALYTICS_KEY:
            return {'GOOGLE_ANALYTICS_KEY': settings.GOOGLE_ANALYTICS_KEY}
    except AttributeError:
        return {}
