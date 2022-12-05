from django import forms
from .models import User, Pet, AuthPhone
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
    AuthenticationForm,
)
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# 로그인
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = '아이디'

# 회원가입
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "age",
            "gender",
            "phone_num",
            "profile_image",
        ]
        labels = {
            "username": "아이디",
            "age": "나이",
            "gender": "성별",
            "phone_num": "연락처",
            "profile_image": "프로필 이미지",
        }


# 회원 정보 수정
class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label=(""), help_text="")

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "nickname",
            "age",
            "gender",
            "profile_image",
        ]
        labels = {
            "username": "아이디",
            "nickname": "닉네임",
            "age": "나이",
            "gender": "성별",
            "profile_image": "프로필 이미지 변경",
        }


# 비밀번호 변경
class CustomPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=("새 비밀번호"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=None,
    )


# 반려동물 등록
class CustomPetCreationForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["pet_image", "petname", "petage", "petgender", "neutralization"]
        labels = {
            "pet_image": "사진",
            "petname": "이름",
            "petage": "나이",
            "petgender": "성별",
            "neutralization": "중성화 여부",
            "species": "종",
        }


# 반려동물 정보 수정
class CustomPetChangeForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["pet_image", "petname", "petage", "petgender", "neutralization"]
        labels = {
            "pet_image": "사진",
            "petname": "이름",
            "petage": "나이",
            "petgender": "성별",
            "neutralization": "중성화 여부",
            "species": "종",
        }


# 핸드폰 인증
class AuthForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["phone_num"]
        labels = {
            "phone_num": "핸드폰 번호",
        }
