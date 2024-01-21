from django.db import models
from common.models import CommonModel


# Create your models here.
class Room(CommonModel):

    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = "shared_room", "Shared Room"

    name = models.CharField(
        max_length=180,
        default="",
    )

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",  # 이렇게 해주면 더이상 user 는 room_set 을 갖지 않습니다.
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
        related_name="rooms",  # 이렇게 해주면 더이상 user 는 room_set 을 갖지 않습니다.
    )

    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rooms",  # 이렇게 해주면 더이상 user 는 room_set 을 갖지 않습니다.
    )

    def __str__(self):
        return self.name

    def total_amenities(self):
        """방이 가진 편의시설의 수를 반환"""
        return self.amenities.count()

    def rating(room):
        # 방에 대한 리뷰의 갯수를 세는 변수 count를 선언합니다.
        count = room.reviews.count()

        # 만약 리뷰가 하나도 없는 경우 (count가 0인 경우)
        if count == 0:
            return 0

        # 리뷰가 하나 이상 있는 경우
        else:
            # 총 평점을 저장할 변수 total_rating을 0으로 초기화합니다.
            total_rating = 0
            # 방의 모든 리뷰를 반복하여 각 리뷰의 평점을 total_rating에 더합니다.
            for review in room.reviews.all().values("rating"):
                total_rating += review["rating"]

            # 평균 평점을 계산합니다. 이 때, round 함수를 사용하여 소수점 둘째 자리까지 반올림합니다.
            # 총 평점을 리뷰 갯수로 나누어 평균을 구합니다.
            return round(total_rating / count, 2)


class Amenity(CommonModel):

    """Amenity Definiton"""

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(room):
        return room.name

    class Meta:
        verbose_name_plural = "Amenities"
