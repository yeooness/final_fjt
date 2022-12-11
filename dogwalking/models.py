from django.db import models
from accounts.models import Pet
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager

# from care.models import Care, Review
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Dogwalking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="pet",
        null=True,
    )
    # condition = models.ForeignKey(Care, on_delete=models.CASCADE, null=True,)
    # 내 위치 주소 입력 모델로 수정 필요
    location = models.CharField(max_length=50)
    # 산책 인원 추가
    members = models.IntegerField(null=True, default=1)
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 90},
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    tags = TaggableManager(blank=True)
    like_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_dogwalking", blank=True
    )
    # 글 내림 판단 여부
    writing_down = models.BooleanField(default=False)
    # 산책 정원
    walking_member = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9)],
        help_text="0~9사이 값으로 입력하세요",
        )
    # 산책 신청 인원
    walking = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="walker")

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


class Review(models.Model):
    grade_choices = (
        ("1", "⭐"),
        ("2", "⭐⭐"),
        ("3", "⭐⭐⭐"),
        ("4", "⭐⭐⭐⭐"),
        ("5", "⭐⭐⭐⭐⭐"),
    )
    grade = models.CharField(max_length=2, choices=grade_choices)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="review_user",
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    review_image = ProcessedImageField(
        null=True,
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 90},
    )
    # 산책날짜
    dogwalking_date = models.DateField(blank=True)
    # 산책장소
    place = models.CharField(max_length=50)
    dogwalking = models.ForeignKey(
        Dogwalking,
        on_delete=models.CASCADE,
        null=True,
    )


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    dogwalking = models.ForeignKey(Dogwalking, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="comment_user",
    )
