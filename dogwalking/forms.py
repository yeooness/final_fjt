from django import forms
from .models import Dogwalking, Review, Comment
from django.forms.widgets import NumberInput


class DogwalkingForm(forms.ModelForm):
    class Meta:
        model = Dogwalking
        fields = [
            "title",
            "area",
            "walking_member",
            "content",
            "image",
            "tags",
        ]
        labels = {
            "title": "제목",
            "area": "지역",
            "content": "내용",
            "image": "이미지",
            "tags": "태그",
        }


class ReviewForm(forms.ModelForm):
    dogwalking_date = forms.DateTimeField(widget=NumberInput(attrs={"type": "date"}))

    class Meta:
        model = Review
        fields = [
            "user",
            "content",
            "dogwalking_date",
            "place",
        ]
        labels = {
            "user": "같이 산책 한 친구",
            "dogwalking_date": "산책 날짜",
            "place": "산책 장소",
            "content": "산책 후기",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
