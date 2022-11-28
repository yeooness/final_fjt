from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Pet
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm
from django.contrib.auth import authenticate, update_session_auth_hash, get_user_model, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import secrets, requests

# Create your views here.

# 회원가입
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = form.save(commit=False)
            user.address = (
                request.POST.get('postcode')
                + request.POST.get('address')
                + request.POST.get('detailAddress')
                + request.POST.get('extraAddress')
            )
            user.save()
            # 자동 로그인
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    context = {
        'form'  : form
    }
    return render(request, 'accounts/signup.html', context)


# 로그인
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)


#로그아웃
def logout(request):
    auth_logout(request)
    return redirect('/')


# 회원정보 페이지
def detail(request, user_pk):
    # 회원 정보
    user = get_object_or_404(get_user_model(), pk=user_pk)
    # 반려동물 정보
    user_pets = Pet.objects.filter(user__id=user_pk)
    # 작성한 게시글
    # user_boards = 
    # 작성한 후기
    # user_reviews = 
    # 팔로워 목록
    user_followers = user.followers.order_by('pk')
    # 팔로잉 목록
    user_followings = user.followings.order_by('pk')
    context = {
        'user' : user,
        'user_pets' : user_pets,
        # 'user_boards' : user_boards,
        # 'user_reviews' : user_reviews,
        'user_followers' : user_followers,
        'user_followings' : user_followings
    }
    return render(request, 'accounts/detail.html', context)


# 회원 정보 수정
def update(request, user_pk):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            user = form.save(commit=False)
            user.address = (
                request.POST.get('postcode')
                + request.POST.get('address')
                + request.POST.get('detailAddress')
                + request.POST.get('extraAddress')
            )
            user.save()
            return redirect('accounts:detail', user_pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/update.html')


# 회원 탈퇴
def delete(request, user_pk):
    user = User.objects.get(pk=user_pk)
    user.delete()
    auth_logout(request)
    return redirect('/')


# 비밀번호 변경
@login_required
def passwordchange(request, user_pk):
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # 변경된 비밀번호로 로그인 유지
            update_session_auth_hash(request, request.user)
            return redirect('accounts:detail', user_pk)
    else:
        form = CustomPasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/passwordchange.html', context)