"""
WSGI config for projeto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
>>>>>>> f211731afb96136b07890dce3e5a6ce2860bea19
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

application = get_wsgi_application()
