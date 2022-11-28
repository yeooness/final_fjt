from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class User(AbstractUser):
    pass
    # 주소
    address = models.CharField(max_length=250)
    # 연락처
    phone_numRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]-?([0-9]{3,4})-?([0-9]{4})$')
    phone_num = models.CharField(validators=[phone_numRegex], max_length=11, blank=True, null=True, default="")
    # 팔로우
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # 프로필 이미지
    profile_image = ProcessedImageField(
        upload_to="images/accounts/",
        blank=True,
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality" : 100}
    )
    # 소셜 회원가입/로그인
    kakao_id = models.BigIntegerField(null=True, unique=True)
    naver_id = models.CharField(null=True, unique=True, max_length=100)
    google_id = models.CharField(null=True, unique=True, max_length=100)