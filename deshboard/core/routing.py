from django.urls import path
from .consumers import GraphConsumer,GraphConsumer1,GraphConsumer2,GraphConsumer3
from .consumers import GraphConsumer4
from .consumerpred import *

ws_urlpatterns = [
    path("ws/graph/",GraphConsumer.as_asgi()),
    path("ws/graph1/",GraphConsumer1.as_asgi()),
    path("ws/graph2/",GraphConsumer2.as_asgi()),
    path("ws/graph3/",GraphConsumer3.as_asgi()),
    path("ws/graph4/",GraphConsumer4.as_asgi()),
    
    path("ws/g1/",GraphConsumer11.as_asgi()),
    
    path("ws/g2/",GraphConsumer111.as_asgi()),
    path("ws/g3/",GraphConsumer21.as_asgi()),
    path("ws/g4/",GraphConsumer31.as_asgi()),
    path("ws/g5/",GraphConsumer41.as_asgi()),
    
    
]