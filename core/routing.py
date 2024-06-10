from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import chat.routing


application = ProtocolTypeRouter({
  # HTTP requests handled by the default Django view handler
  "http": get_asgi_application(),
  # WebSocket connections routed to your chat application
  "websocket": AuthMiddlewareStack(
      URLRouter(
          chat.routing.websocket_urlpatterns
      )
  ),
})

