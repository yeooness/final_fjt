from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.urls import reverse
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone
from accounts.models import Pet


class Event(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    event_board_choices = [
        ("일기", "일기"),
        ("산책일기", "산책일기"),
        ("건강일기", "건강일기"),
    ]
    journal_board = models.CharField(max_length=20, choices=event_board_choices)
    title = models.CharField(max_length=200)
    description = models.TextField()
    # 산책
    route = models.TextField(null=True)
    consumed_calories = models.IntegerField(null=True)
    walking_time = models.IntegerField(null=True)
    # 데일리
    content = models.TextField(null=True)
    image = ProcessedImageField(
        upload_to="images/daily_journal/",
        blank=True,
        processors=[ResizeToFill(400, 400)],
        format="JPEG",
        options={"quality": 80},
    )
    # 건강
    meals = models.CharField(max_length=100, null=True)
    energy = models.CharField(max_length=100, null=True)
    medicine = models.CharField(max_length=100, null=True)
    # 작성시간
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    # end_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("calendarapp:event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("calendarapp:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.content} </a>'

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


# 산책일지
class Dogwalking_Journal(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    route = models.TextField()
    consumed_calories = models.IntegerField()
    walking_time = models.IntegerField()
    start_time = models.DateTimeField()
    # end_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.route

    def get_absolute_url(self):
        return reverse("calendarapp:event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("calendarapp:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.route} </a>'


class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        unique_together = ["event", "user"]

    def __str__(self):
        return str(self.user)
