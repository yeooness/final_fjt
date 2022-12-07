import os, time, base64, hmac, hashlib, requests
from django.db import models
from dotenv import load_dotenv
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.


class User(AbstractUser):
    # 아이디
    username = models.CharField(
        max_length=25,
        unique=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={"unique": "이미 사용중인 아이디입니다."},
    )
    # 닉네임
    nickname = models.CharField(max_length=25, unique=True)
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
        validators=[phone_numRegex],
        max_length=11,
        blank=True,
    )
    is_phone_active = models.BooleanField(default=False)
    # 팔로우
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    # 차단
    block = models.ManyToManyField("self", symmetrical=False, related_name="blockers")
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

    # 알람
    pet_notice = models.BooleanField(default=True)
    note_notice = models.BooleanField(default=True)
    notice_pet = models.BooleanField(default=True)
    notice_note = models.BooleanField(default=True)


class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pet")
    # 이미지
    pet_image = ProcessedImageField(
        upload_to="images/accounts_pet/",
        blank=True,
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality": 100},
    )
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
    breeds = models.CharField(max_length=100)
    birthday = models.DateField()


# 핸드폰 인증
load_dotenv()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuthPhone(TimeStampedModel):
    phone = models.CharField(
        max_length=11,
        validators=[RegexValidator(r"^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$")],
        primary_key=True,
        verbose_name="휴대폰 번호",
    )
    auth_number = models.IntegerField(verbose_name="인증 번호")

    NAVER_CLOUD_ACCESS_KEY = os.getenv("NAVER_CLOUD_ACCESS_KEY")
    NAVER_CLOUD_SECRET_KEY = os.getenv("NAVER_CLOUD_SECRET_KEY")
    NAVER_CLOUD_SERVICE_ID = os.getenv("NAVER_CLOUD_SERVICE_ID")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.send_sms()

    def send_sms(self):
        timestamp = str(int(time.time() * 1000))
        access_key = self.NAVER_CLOUD_ACCESS_KEY
        secret_key = bytes(self.NAVER_CLOUD_SECRET_KEY, "UTF-8")
        service_id = self.NAVER_CLOUD_SERVICE_ID
        method = "POST"
        uri = f"/sms/v2/services/{service_id}/messages"
        message = method + " " + uri + "\n" + timestamp + "\n" + access_key
        message = bytes(message, "UTF-8")
        signing_key = base64.b64encode(
            hmac.new(secret_key, message, digestmod=hashlib.sha256).digest()
        )
        url = f"https://sens.apigw.ntruss.com/sms/v2/services/{service_id}/messages"
        data = {
            "type": "SMS",
            "from": "01095983520",
            "content": f"[당근집사] 인증 번호 [{self.auth_number}] 입력해주세요.",
            "messages": [{"to": f"{self.phone}"}],
        }
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "x-ncp-apigw-timestamp": timestamp,
            "x-ncp-iam-access-key": access_key,
            "x-ncp-apigw-signature-v2": signing_key,
        }
        requests.post(url, json=data, headers=headers)
