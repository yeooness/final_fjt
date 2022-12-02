from django.contrib import admin
from .models import DailyJournal, DogwalkingJournal, HealthJournal

# Register your models here.
admin.site.register(DailyJournal)
admin.site.register(DogwalkingJournal)
admin.site.register(HealthJournal)
