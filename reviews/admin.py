from django.contrib import admin
from .models import Review


# Register your models here.
class WordFilter(admin.SimpleListFilter):
    # 필터의 제목을 정의합니다. 이 제목이 관리자 페이지에서 보여집니다.
    title = "Filter by words!"

    # URL에서 사용될 파라미터의 이름을 정의합니다.
    parameter_name = "word"

    # 필터 옵션을 정의하는 메서드입니다.
    # 관리자 페이지에서 선택할 수 있는 필터 옵션을 리스트로 반환합니다.
    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),  # "Good"이라는 레이블을 가진 "good" 필터 옵션
            ("great", "Great"),  # "Great"이라는 레이블을 가진 "great" 필터 옵션
            ("awesome", "Awesome"),  # "Awesome"이라는 레이블을 가진 "awesome" 필터 옵션
        ]

    # 선택된 필터에 따라 쿼리셋을 필터링하는 메서드입니다.
    def queryset(self, request, reviews):
        # 현재 선택된 필터 값(예: "good", "great", "awesome")을 가져옵니다.
        word = self.value()
        # 만약 필터 값이 설정되어 있다면 해당 단어를 포함하는 리뷰들만 필터링합니다.
        if word:
            return reviews.filter(payload__contains=word)
        # 필터 값이 설정되어 있지 않다면 모든 리뷰를 반환합니다.
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",  # 만약 작성한 모델의 str 메서드를 보여주길 원한다면 이렇게 작성해주면 됩니다.
        "payload",
    )
    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
