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


# 산책요청
class Alarm(models.Model):
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_from_dw"
    )
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_to_dw"
    )
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    garbage = models.BooleanField(default=False)
