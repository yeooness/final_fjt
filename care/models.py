from django.db import models
from accounts.models import Pet
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Care(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="care_pet",
        null=True,
    )
    # condition = models.
    # 내 위치 주소 입력 모델로 수정 필요
    # location = models.CharField(max_length=50)
    title = models.CharField(verbose_name='title',max_length=30)
    content = models.TextField(verbose_name='content',)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 90},
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    like_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_care", blank=True
    )

    caring_animal = models.CharField(verbose_name='caring_animal', max_length=300, default='') # 돌봄 가능 동물
    caring_time = models.CharField(verbose_name='caring_time',max_length=300) # 돌봄 가능 기간
    etc = models.CharField(verbose_name='etc',max_length=300) # 기타

    area_choices = [
        ("경기도", "경기도"),
        ("서울시", "서울시"),
        ("부산광역시", "부산광역시"),
        ("경상남도", "경상남도"),
        ("인천광역시", "인천광역시"),
        ("경상북도", "경상북도"),
        ("대구광역시", "대구광역시"),
        ("충청남도", "충청남도"),
        ("전라남도", "전라남도"),
        ("전라북도", "전라북도"),
        ("충청북도", "충청북도"),
        ("강원도", "강원도"),
        ("대전광역시", "대전광역시"),
        ("광주광역시", "광주광역시"),
        ("울산광역시", "울산광역시"),
        ("제주도", "제주도"),
        ("세종시", "세종시"),
    ]

    area = models.CharField(
        max_length=100,
        choices=area_choices,
        default="선택",
    )

    gender_choices = [
    ("남자", "남자"),
    ("여자", "여자"),
    ("상관없음", "상관없음")
    ]

    gender = models.CharField(
        max_length=20,
        choices=gender_choices,
        default="선택",
    )

class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="care_review_user",
    )
    content = models.TextField()
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    care = models.ForeignKey(Care, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="care_comment_user",
    )
