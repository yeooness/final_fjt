from django import forms
from .models import Care, Review, Comment


class Careform(forms.ModelForm):
    class Meta:
        model = Care
        fields = [
            "title",
            "content",
            "image",
        ]
        labels = {
            "title": "제목",
            "content": "내용",
            "image": "이미지",
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
