from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from django.urls import re_path
from logger.consumer import LoggerConsumer

application = ProtocolTypeRouter(
    {
        "websocket": AuthMiddlewareStack(
            URLRouter([re_path(r"logger/$", LoggerConsumer)])
        )
    }
)
