from django.db import models

# from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# from accounts.models import Pet
# Create your models here.
class Journal(models.Model):
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    # )
    # pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DogwalkingJournal(models.Model):
    date = models.DateField(auto_now_add=True)
    route = models.TextField()
    consumed_calories = models.IntegerField()
    walking_time = models.IntegerField()


class DailyJournal(models.Model):
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    # image = models.ProcessedImageField(
    #     upload_to="images/daily_journal/",
    #     blank=True,
    #     processors=[ResizeToFill(400, 400)],
    #     format="JPEG",
    #     options={"quality": 80},
    # )


class HealthJournal(models.Model):
    date = models.DateField(auto_now_add=True)
    meals = models.CharField(max_length=100)
    energy = models.TextField()
    medicine = models.CharField(max_length=100)
    time = models.DateTimeField()
