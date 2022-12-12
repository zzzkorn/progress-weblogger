from logger.filters import MessageFilter
from logger.models import Message
from logger.serializers.message import MessageSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin


class MessageListView(GenericAPIView, ListModelMixin):
    queryset = Message.objects.all().order_by("-id")
    serializer_class = MessageSerializer
    filterset_class = MessageFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
