from logger.filters import DeviceFilter
from logger.models import Device
from logger.serializers.device import DeviceSerializer
from rest_framework import permissions
from rest_framework import viewsets


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API эндпоинт для чтения и редактировая Device
    """

    queryset = Device.objects.all().order_by("-id")
    serializer_class = DeviceSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None
    http_method_names = ["post", "get", "put", "delete"]
    filterset_class = DeviceFilter
