"""
WSGI config for sampleproj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sampleproj.settings")


application = get_wsgi_application()
if settings.HEROKU:
    application = Cling(application)
