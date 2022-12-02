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
    like_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_care", blank=True
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
