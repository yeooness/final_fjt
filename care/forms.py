from django import forms
from .models import Care, Review, Comment
from django.forms.widgets import NumberInput

# CARING_ANIMAL = [
#     ('고양이', '고양이'),
#     ('강아지', '강아지'),
#     ]

# CARING_TIME = [
#     ('4시간이하', "4시간이하"),
#     ("1일이하", "1일이하"),
#     ("3일이하", "3일이하"),
#     ("7일이하", "7일이하"),
#     ("7일초과", "7일초과"),
# ]

# ETC = [
#     ('사전만남 가능', '사전만남가능'),
#     ('반려동물 있음', '반려동물 있음'),
#     ('노견/노묘 케어 가능', '노견/노묘 케어 가능'),
#     ('픽업 가능', '픽업 가능'),
#     ('산책 가능', '산책 가능'),
#     ('돌봄 경력 있음', '돌봄 경력 있음'),
# ]


class Careform(forms.ModelForm):
    # caring_animal = forms.MultipleChoiceField(
    # choices=CARING_ANIMAL,
    # widget=forms.CheckboxSelectMultiple()
    # )

    # caring_time = forms.MultipleChoiceField(
    # choices=CARING_TIME,
    # widget=forms.CheckboxSelectMultiple()
    # )

    # etc = forms.MultipleChoiceField(
    # choices=ETC,
    # widget=forms.CheckboxSelectMultiple()
    # )

    class Meta:
        model = Care
        fields = [
            "title",
            "area",
            "content",
            "image",
        ]
        labels = {
            "title": "제목",
            "area": "지역",
            "content": "내용",
            "image": "이미지",
        }


class ReviewForm(forms.ModelForm):
    caring_date = forms.DateTimeField(widget=NumberInput(attrs={"type": "date"}))

    class Meta:
        model = Review
        fields = [
            "content",
            "caring_date",
        ]
        labels = {
            "caring_date": "돌봄 기간",
            "content": "돌봄 후기",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
