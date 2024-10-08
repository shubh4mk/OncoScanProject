import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter

# Set the default settings module for the 'asgi' application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OncoScan.settings")

# Initialize the Django ASGI application
django_asgi_app = get_asgi_application()

# Define the application using ProtocolTypeRouter
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # Add other protocols (like WebSocket) here later if needed
})
