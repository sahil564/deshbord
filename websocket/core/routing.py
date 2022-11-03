import imp
from django.urls import path

from core import consumers1
from . import consumers

websocket_urlpatterns =[
    path("ws/sc/",consumers.MySyncConsumer.as_asgi()),
    #path("ws/ac/",consumers.MyAsyncConsumer.as_asgi()),
    path("ws/ac/",consumers1.MyAsyncConsumer.as_asgi()),
]