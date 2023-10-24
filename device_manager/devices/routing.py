from django.urls import re_path

from . import consumer

websocket_urlpatterns = [
    re_path(r'ws/device/(?P<device_id>\w+)/$', consumer.DeviceConsumer.as_asgi()),
]

