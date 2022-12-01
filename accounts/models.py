from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.


class User(AbstractUser):
    pass
    # 이름
    last_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    # 나이
    age = models.IntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    # 성별
    GENDER_CHOICES = ((None, "선택"), ("M", "남자"), ("W", "여자"))
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default="선택")
    # 주소
    address = models.CharField(max_length=250)
    # 연락처
    phone_numRegex = RegexValidator(
        regex=r"^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$"
    )
    phone_num = models.CharField(
        validators=[phone_numRegex], max_length=11, blank=True, null=True, default=""
    )
    # 팔로우
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    # 프로필 이미지
    profile_image = ProcessedImageField(
        upload_to="images/accounts/",
        blank=True,
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality": 100},
    )
    # 소셜 회원가입/로그인
    kakao_id = models.BigIntegerField(null=True, unique=True)
    naver_id = models.CharField(null=True, unique=True, max_length=100)
    google_id = models.CharField(null=True, unique=True, max_length=100)

    # 좋아요
    liking = models.ManyToManyField("self", symmetrical=False, related_name="like")


class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pet")
    # 반려동물 이름
    petname = models.CharField(max_length=25)
    # 반려동물 나이
    petage = models.IntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    # 반려동물 성별
    PETGENDER_CHOICES = ((None, "선택"), ("M", "남아"), ("F", "여아"))
    petgender = models.CharField(max_length=2, choices=PETGENDER_CHOICES, default="선택")
    # 중성화 여부
    NEUTRALIZATION_CHOICES = ((None, "선택"), ("Y", "중성화 완료"), ("N", "중성화 전"))
    neutralization = models.CharField(
        max_length=2, choices=NEUTRALIZATION_CHOICES, default="선택"
    )
    # 종
    SPECIES_CHOICES = (
        (None, "선택"),
        ("dog", "강아지"),
        ("cat", "고양이"),
    )
    species = models.CharField(max_length=3, choices=SPECIES_CHOICES, default="선택")
