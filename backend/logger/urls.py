from django.urls import include
from django.urls import path
from logger.views.device import DeviceViewSet
from logger.views.message import MessageListView
from rest_framework import routers

device_router = routers.DefaultRouter()
device_router.register(r"devices", DeviceViewSet)

urlpatterns = [
    path("messages/", MessageListView.as_view()),
    path("", include(device_router.urls)),
]
