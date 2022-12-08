from django import forms
from .models import Dogwalking, Review, Comment, Alarm


class DogwalkingForm(forms.ModelForm):
    class Meta:
        model = Dogwalking
        fields = [
            "title",
            "members",
            "content",
            "image",
            "tags",
        ]
        labels = {
            "title": "제목",
            "members": "산책 인원",
            "content": "내용",
            "image": "이미지",
            "tags": "태그",
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]


class AlarmForm(forms.ModelForm):
    class Meta:
        model = Alarm
        fields = ("title", "content")
        labels = {
            "title": "제목",
            "content": "내용",
        }
