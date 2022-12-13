from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone


class Calendar(models.Model):
    userId = models.IntegerField(default=0)  # 사용자 아이디 (Admin users 테이블의 PK)
    title = models.CharField(max_length=100)  # 이벤트 제목
    start = models.DateTimeField("Start Date")  # 이벤트 시작일시
    end = models.DateTimeField("End Date")  # 이벤트 종료일시
    allDay = models.BooleanField(default=True)  # 이벤트가 종일 지속되는지 여부

    def __str__(self) -> str:
        return self.title
