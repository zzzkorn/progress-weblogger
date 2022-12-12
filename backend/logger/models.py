from django.db import models


class Device(models.Model):
    ip_address = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        verbose_name="Адресс устройства",
    )

    description = models.CharField(
        max_length=200,
        default="Неизвестное устройство",
        verbose_name="Описание устройства",
        null=True,
    )

    @property
    def message_count(self):
        return Message.objects.filter(device=self).count()

    def __str__(self):
        if self.description:
            return f"{self.ip_address} {self.description}"
        return f"{self.ip_address}"

    def __repr__(self):
        if self.description:
            return f"{self.ip_address} {self.description}"
        return f"{self.ip_address}"

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"


class Message(models.Model):
    MESSAGE_TYPE = (
        ("packet", "data packet"),
        ("info", "info or debug message"),
        ("error", "error message"),
    )
    PACKET_TYPE = (
        ("received", "received packet"),
        ("sent", "sent packet"),
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время получения",
    )
    device = models.ForeignKey(
        Device,
        on_delete=models.SET_NULL,
        related_name="device",
        verbose_name="К какому устройству относится сообщение",
        null=True,
    )
    raw_data = models.BinaryField(
        verbose_name="Данные в сыром виде",
        null=True,
    )
    data = models.TextField(verbose_name="Данные", null=True)
    message_type = models.CharField(
        max_length=12,
        choices=MESSAGE_TYPE,
        verbose_name="Тип сообщения",
    )
    packet_type = models.CharField(
        max_length=12,
        choices=PACKET_TYPE,
        verbose_name="Тип пакета",
        null=True,
    )

    def __get_str(self):
        message = (
            f"{self.timestamp}.{self.message_type}.{self.packet_type}: "
            f"{self.data or self.raw_data}"
        )
        return message

    @property
    def transcribed(self):
        if self.data:
            return True
        return False

    transcribed.fget.short_description = "Извлечены ли даннные из сырых данных"

    def __str__(self):
        return self.__get_str()

    def __repr__(self):
        return self.__get_str()

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
