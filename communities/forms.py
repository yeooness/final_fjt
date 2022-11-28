from django import forms
from .models import Community

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = [
            "title",
            "content",
            "image",
            "community",
        ]

        labels = {
            "community": "게시판 선택",
            "title": "제목",
            "content": "내용",
            "image": "이미지",
        }