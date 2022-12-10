from django.db import models

# Create your models here.


class Information(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # 자유 후기 질문 지식 4개 카테고리 형식
    information_choices = [
        ("반려동물 동반 식당", "반려동물 동반 식당"),
        ("반려동물 동반 카페", "반려동물 동반 카페"),
        ("동물병원", "동물병원"),
    ]

    information = models.CharField(
        max_length=20,
        choices=information_choices,
        default="선택",
    )