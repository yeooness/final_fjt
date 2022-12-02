from django.db import models

# from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from accounts.models import Pet, User
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.


class DogwalkingJournal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    route = models.TextField()
    consumed_calories = models.IntegerField()
    walking_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 작성 시간
    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        # elif time < timedelta(days=2):
        #     time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
        #     return str(time.days) + '일 전'
        else:
            return False


class DailyJournal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    image = models.ImageField(
        upload_to="images/daily_journal/",
        blank=True,
        # processors=[ResizeToFill(400, 400)],
        # format="JPEG",
        # options={"quality": 80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 작성 시간
    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        # elif time < timedelta(days=2):
        #     time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
        #     return str(time.days) + '일 전'
        else:
            return False


class HealthJournal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    meals = models.CharField(max_length=100)
    energy = models.CharField(max_length=100)
    medicine = models.CharField(max_length=100)
    # time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 작성 시간
    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        # elif time < timedelta(days=2):
        #     time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
        #     return str(time.days) + '일 전'
        else:
            return False
