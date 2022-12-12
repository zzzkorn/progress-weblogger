from django_filters import CharFilter
from django_filters import DateTimeFromToRangeFilter
from django_filters import FilterSet
from django_filters import NumberFilter
from logger.models import Device
from logger.models import Message


class MessageFilter(FilterSet):
    from_timestamp = DateTimeFromToRangeFilter(
        field_name="timestamp",
        lookup_expr="gte",
    )
    to_timestamp = DateTimeFromToRangeFilter(
        field_name="timestamp",
        lookup_expr="lte",
    )
    device = NumberFilter()

    class Meta:
        model = Message
        fields = ["from_timestamp", "to_timestamp", "device"]


class DeviceFilter(FilterSet):
    ip_address = CharFilter(lookup_expr="startswith")

    class Meta:
        model = Device
        fields = ["ip_address"]
