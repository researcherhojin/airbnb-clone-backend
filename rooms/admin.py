from django.contrib import admin
from .models import Room, Amenity


# Register your models here.
# 'Set all prices to zero'라는 설명을 가진 관리자 액션을 등록합니다.
@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    # 전달된 rooms queryset에 대해 각 room 객체를 순회합니다.
    for room in rooms.all():
        room.price = 0  # room의 가격을 0으로 설정합니다.
        room.save()  # 변경 사항을 데이터베이스에 저장합니다.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)  # 위에서 정의한 reset_prices 액션을 관리자 페이지에서 사용할 수 있도록 설정합니다.

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",  # review 갯수 카운팅
        "owner",
        "created_at",
        # "updated_at",
    )

    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",  # 'name' 필드를 기준으로 검색을 수행합니다.
        "^price",  # '^' 기호는 'price' 필드에 대해 접두어 검색을 의미합니다.
        # 이는 검색어가 'price' 필드의 시작 부분과 일치할 때 해당하는 결과를 찾습니다.
        "=owner__username",  # '=' 기호는 정확한 일치를 의미합니다.
        # 'owner__username' 필드의 값이 검색어와 정확히 일치하는 경우에 해당 결과를 찾습니다.
        # 여기서 '__' (더블 언더스코어)는 관계된 모델의 필드를 나타내는데 사용됩니다.
        # 즉, 'owner' 모델의 'username' 필드를 기준으로 검색합니다.
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
