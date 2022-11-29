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
    # pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="pet")
    #     condition = models.ForeignKey(Care, on_delete=models.CASCADE)
    # grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # 내 위치 주소 입력 모델로 수정 필요
    location = models.CharField(max_length=50)
    # 산책 인원 추가
    members = models.IntegerField(null=True)
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


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    content = models.TextField()
    # grade = models.ForeignKey(
    #     Dogwalking,
    #     on_delete=models.CASCADE,
    # )
