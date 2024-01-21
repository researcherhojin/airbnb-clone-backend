from django.db import models
from common.models import CommonModel

# Create your models here.


class Booking(CommonModel):

    """Booking Model Definition"""

    class BookingKindChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices.choices,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # 유저가 사라지면 예약도 사라지도록!
        related_name="bookings",  # 유저의 예약들을 알 수 있도록!
    )
    room = models.ForeignKey(  # 예약은 1명이 1개씩 할 수 있도록!
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  # 유저 정보가 남아 있다면 방이 삭제 되더라도 로그 표시
        related_name="bookings",  # 방의 예약들을 알 수 있도록!
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookings",  # 경험의 예약들을 알 수 있도록!
    )
    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )
    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.kind.title()} booking for: {self.user}"
