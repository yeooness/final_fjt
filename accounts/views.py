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

# 소셜 로그인 연동
state_token = secrets.token_urlsafe(16)

# 카카오 로그인
def kakao_request(request):
    kakao_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
    redirect_uri = 'http://localhost:8000/accounts/login/kakao/callback'
    client_id = '3044dd3e42caed2e8e6ed2f4650c22f7' # 배포시 보안 적용
    return redirect(f'{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}')

def kakao_callback(request):
    data = {
        'grant_type' : 'authorization_code',
        'client_id' : '3044dd3e42caed2e8e6ed2f4650c22f7',
        'redirect_uri' : 'http://localhost:8000/accounts/login/kakao/callback',
        'code' : request.GET.get('code'),
    }
    kakao_token_api = 'https://kauth.kakao.com/oauth/token'
    access_token = requests.post(kakao_token_api, data=data).json()['access_token']

    headers = {'Authorization' : f'bearer ${access_token}'}
    kakao_user_api = "https://kapi.kakao.com/v2/user/me"
    kakao_user_information = requests.get(kakao_user_api, headers=headers).json()

    kakao_id = kakao_user_information['id']
    kakao_nickname = kakao_user_information['properties']['nickname']
    kakao_profile_image = kakao_user_information['properties']['profile_image']

    if get_user_model().objects.filter(kakao_id=kakao_id).exists():
        kakao_user = get_user_model().objects.get(kakao_id=kakao_id)
    else:
        kakao_login_user = get_user_model()
        kakao_login_user.username = kakao_nickname
        kakao_login_user.kakao_id = kakao_id
        kakao_login_user.social_profile_picture = kakao_profile_image
        kakao_login_user.set_password(str(state_token))
        kakao_login_user.save()
        kakao_user = get_user_model().objects.get(kakao_id=kakao_id)
    auth_login(request, kakao_user, "django.contrib.auth.backends.ModelBackend")
    return redirect(request.GET.get('next') or '/')


# 네이버 로그인
def naver_request(request):
    naver_api = "https://nid.naver.com/oauth2.0/authorize?response_type=code"
    client_id = 'rbVOoAEithFIkqeqIciW' # 배포시 보안 적용
    redirect_uri = 'http://localhost:8000/accounts/login/naver/callback'
    state_token = secrets.token_urlsafe(16)
    return redirect(f'{naver_api}&client_id={client_id}&redirect_uri={redirect_uri}&')
