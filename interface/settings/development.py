LOCAL_SETTINGS = True
from interface.settings.base import *

SITE_ID = 1

SECRET_KEY = 'asdasda@132'

# define environment
STAGE_NAME = 'DEV'  # either PROD or DEV

# debugging changes according to environment configuration
if STAGE_NAME == 'DEV':
    DEBUG = True
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    DEBUG = False
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'interface',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '',
    }
}

# use sqlite for testing
if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

CACHES = {
    'default': dict(
        BACKEND='johnny.backends.filebased.FileBasedCache',
        LOCATION=PROJECT_DIR + '/../tmp/django_cache',
        JOHNNY_CACHE=True,
    )
}
JOHNNY_MIDDLEWARE_KEY_PREFIX = 'jc_ts'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_URL = 'http://127.0.0.1:8000/media/'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

