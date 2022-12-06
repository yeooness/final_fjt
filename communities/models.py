from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from taggit.managers import TaggableManager

# Create your models here.


class Community(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # 자유 후기 질문 지식 4개 카테고리 형식
    community_choices = [
        ("자유게시판", "자유게시판"),
        ("후기게시판", "후기게시판"),
        ("질문게시판", "질문게시판"),
    ]

    community = models.CharField(
        max_length=20,
        choices=community_choices,
        default="선택",
    )

    pet_species_choices = [
        ("강아지", "강아지"),
        ("고양이", "고양이"),
    ]

    pet_species = models.CharField(
        max_length=20,
        choices=pet_species_choices,
        default="선택",
    )

    review_board_choices = [
        ("용품 후기", "용품 후기"),
        ("박람회 후기", "박람회 후기"),
        ("병원 후기", "병원 후기"),
    ]

    review_board = models.CharField(
        max_length=20,
        choices=review_board_choices,
        default="선택",
    )

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 90},
    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_communities", blank=True
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)


class Comment(models.Model):
    content = models.TextField(max_length=300, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
