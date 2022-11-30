from django import forms
from .models import Community, Comment


class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = [
            "community",
            "title",
            "content",
            "image",
            "tags",
        ]

        labels = {
            "community": "게시판 선택",
            "title": "제목",
            "content": "내용",
            "image": "이미지",
            "tags": "태그",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ("community", "user")

        labels = {
            "content": "댓글",
        }


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label="Search Word")
