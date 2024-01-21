from django.db import models
from common.models import CommonModel

# Create your models here.


class Wishlist(CommonModel):

    """Wishlist Model Definition"""

    name = models.CharField(
        max_length=150,
    )
    rooms = models.ManyToManyField(
        "rooms.Room",
        related_name="wishlists",  # 이렇게 해주면 더이상 room 은 wishlist_set 을 갖지 않습니다.,
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
        related_name="wishlists",  # 이렇게 해주면 더이상 experience 는 wishlist_set 을 갖지 않습니다.,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="wishlists",  # 이렇게 해주면 더이상 user 는 wishlist_set 을 갖지 않습니다.,
    )

    def __str__(self):
        return self.name
