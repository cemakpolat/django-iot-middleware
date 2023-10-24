import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from devices.routing import websocket_urlpatterns
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'device_manager.settings')
django.setup()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )),
})

