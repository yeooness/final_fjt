from django import forms
from .models import *


class DailyJournalForm(forms.ModelForm):
    class Meta:
        model = DailyJournal
        fields = [
            # "journal_board",
            "content",
            "image",
        ]
        labels = {
            # "journal_board": "작성할 일기",
            "content": "내용",
            "image": "사진",
        }


class DogwalkingJournalForm(forms.ModelForm):
    class Meta:
        model = DogwalkingJournal
        fields = [
            "route",
            "consumed_calories",
            "walking_time",
        ]
        labels = {
            "route": "산책 경로",
            "consumed_calories": "소모된 칼로리",
            "walking_time": "산책에 소요된 시간",
        }


class HealthJournalForm(forms.ModelForm):
    class Meta:
        model = HealthJournal
        fields = [
            "meals",
            "energy",
            "medicine",
            # "time",
        ]
        labels = {
            "meals": "급여",
            "energy": "활력",
            "medicine": "약",
            # "time": "급여/약 시간",
        }
