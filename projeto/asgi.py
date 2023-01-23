"""
ASGI config for projeto project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
>>>>>>> f211731afb96136b07890dce3e5a6ce2860bea19
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

application = get_asgi_application()
