from django import forms
from .models import Dogwalking, Review, Comment
from django.forms.widgets import NumberInput


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
        fields = [
            "content",
            "dogwalking_date",
            "place",
            "grade",
        ]
        labels = {
            "dogwalking_date": "산책 날짜",
            "place": "산책 장소",
            "content": "산책 후기",
            "grade": "산책에 대한 평점",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
