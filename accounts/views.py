import secrets, requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Pet
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
    CustomPasswordChangeForm,
    CustomPetCreationForm,
    CustomPetChangeForm,
)
from django.contrib.auth import (
    authenticate,
    update_session_auth_hash,
    get_user_model,
    login as auth_login,
    logout as auth_logout,
)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse

# Create your views here.


# 회원가입
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.address = (
                request.POST.get("postcode")
                + request.POST.get("address")
                + request.POST.get("detailAddress")
                + request.POST.get("extraAddress")
            )
            user.save()
            # 자동 로그인
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect("communities:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


# 로그인
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("communities:index")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect("communities:index")


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
    user_followers = user.followers.order_by("pk")
    # 팔로잉 목록
    user_followings = user.followings.order_by("pk")
    context = {
        "user": user,
        "user_pets": user_pets,
        # 'user_boards' : user_boards,
        # 'user_reviews' : user_reviews,
        "user_followers": user_followers,
        "user_followings": user_followings,
    }
    return render(request, "accounts/detail.html", context)


# 반려동물 등록
def pet_register(request, user_pk):
    if request.method == "POST":
        form = CustomPetCreationForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomPetCreationForm()
    context = {"form": form}
    return render(request, "accounts/pet_register.html", context)


# 반려동물 정보 수정
def pet_update(request, user_pk, pet_pk):
    pet = get_object_or_404(Pet, pk=pet_pk)
    if request.method == "POST":
        form = CustomPetChangeForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomPetChangeForm(instance=pet)
    context = {
        "form": form,
    }
    return render(request, "accounts/pet_update.html", context)


# 회원 정보 수정
def update(request, user_pk):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.address = (
                request.POST.get("postcode")
                + request.POST.get("address")
                + request.POST.get("detailAddress")
                + request.POST.get("extraAddress")
            )
            user.save()
            return redirect("accounts:detail", user_pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)


# 회원 탈퇴
@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("communities:index")


# 비밀번호 변경
@login_required
def passwordchange(request, user_pk):
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # 변경된 비밀번호로 로그인 유지
            update_session_auth_hash(request, request.user)
            return redirect("accounts:detail", user_pk)
    else:
        form = CustomPasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/passwordchange.html", context)


# 팔로우
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                "is_followed": is_followed,
                "followers_count": you.followers.count(),
                "followings_count": you.followings.count(),
            }
            return JsonResponse(context)
        return redirect("accounts:detail", you.username)
    return redirect("accounts:login")


# 차단
@login_required
def block(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    if user != request.user:
        if user.blockers.filter(pk=request.user.pk).exists():
            user.blockers.remove(request.user)
            user.save()
        else:
            user.blockers.add(request.user)
            user.save()
    return redirect("accounts:detail", user_pk)


@login_required
def block_user(request):
    blockers = request.user.blocking.all()
    context = {"blockers": blockers}
    return render(request, "accounts/block_user.html", context)


@login_required
def block_user_block(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    if user != request.user:
        if user.blockers.filter(pk=request.user.pk).exists():
            user.blockers.remove(request.user)
            user.save()
        else:
            user.blockers.add(request.user)
            user.save()
    return redirect("accounts:block_user")


# 소셜 로그인 연동
state_token = secrets.token_urlsafe(16)

# 카카오 로그인
def kakao_request(request):
    kakao_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
    redirect_uri = (
        "http://localhost:8000/accounts/templates/accounts/login/kakao/callback"
    )
    client_id = "3044dd3e42caed2e8e6ed2f4650c22f7"  # 배포시 보안적용 해야함
    return redirect(f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}")


def kakao_callback(request):
    data = {
        "grant_type": "authorization_code",
        "client_id": "3044dd3e42caed2e8e6ed2f4650c22f7",  # 배포시 보안적용 해야함
        "redirect_uri": "http://localhost:8000/accounts/templates/accounts/login/kakao/callback",
        "code": request.GET.get("code"),
    }
    kakao_token_api = "https://kauth.kakao.com/oauth/token"
    access_token = requests.post(kakao_token_api, data=data).json()["access_token"]

    headers = {"Authorization": f"bearer ${access_token}"}
    kakao_user_api = "https://kapi.kakao.com/v2/user/me"
    kakao_user_information = requests.get(kakao_user_api, headers=headers).json()

    kakao_id = kakao_user_information["id"]
    kakao_nickname = kakao_user_information["properties"]["nickname"]
    kakao_profile_image = kakao_user_information["properties"]["profile_image"]

    if get_user_model().objects.filter(kakao_id=kakao_id).exists():
        kakao_user = get_user_model().objects.get(kakao_id=kakao_id)
    else:
        kakao_login_user = get_user_model()()
        kakao_login_user.username = kakao_nickname
        kakao_login_user.kakao_id = kakao_id
        kakao_login_user.set_password(str(state_token))
        kakao_login_user.save()
        kakao_user = get_user_model().objects.get(kakao_id=kakao_id)
    auth_login(request, kakao_user, backend="django.contrib.auth.backends.ModelBackend")
    return redirect(request.GET.get("next") or "communities:index")


# 네이버 로그인
def naver_request(request):
    naver_api = "https://nid.naver.com/oauth2.0/authorize?response_type=code"
    client_id = "rbVOoAEithFIkqeqIciW"  # 배포시 보안적용 해야함
    redirect_uri = (
        "http://localhost:8000/accounts/templates/accounts/login/naver/callback"
    )
    state_token = secrets.token_urlsafe(16)
    return redirect(
        f"{naver_api}&client_id={client_id}&redirect_uri={redirect_uri}&state={state_token}"
    )


def naver_callback(request):
    data = {
        "grant_type": "authorization_code",
        "client_id": "rbVOoAEithFIkqeqIciW",  # 배포시 보안적용 해야함
        "client_secret": "nq9LZrYX2Y",
        "code": request.GET.get("code"),
        "state": request.GET.get("state"),
        "redirect_uri": "http://localhost:8000/accounts/templates/accounts/login/naver/callback",
    }
    naver_token_request_url = "https://nid.naver.com/oauth2.0/token"
    access_token = requests.post(naver_token_request_url, data=data).json()[
        "access_token"
    ]

    headers = {"Authorization": f"bearer {access_token}"}
    naver_call_user_api = "https://openapi.naver.com/v1/nid/me"
    naver_user_information = requests.get(naver_call_user_api, headers=headers).json()

    naver_id = naver_user_information["response"]["id"]
    naver_nickname = naver_user_information["response"]["nickname"]
    naver_img = naver_user_information["response"]["profile_image"]
    if get_user_model().objects.filter(naver_id=naver_id).exists():
        naver_user = get_user_model().objects.get(naver_id=naver_id)
    else:
        naver_login_user = get_user_model()()
        naver_login_user.username = naver_nickname
        naver_login_user.naver_id = naver_id
        naver_login_user.set_password(str(state_token))
        naver_login_user.image = naver_img
        naver_login_user.is_social = 2
        naver_login_user.save()
        naver_user = get_user_model().objects.get(naver_id=naver_id)
    auth_login(request, naver_user)
    return redirect(request.GET.get("next") or "communities:index")


# 구글 로그인
def google_request(request):
    google_api = "https://accounts.google.com/o/oauth2/v2/auth"
    client_id = "526851643558-otkt8p42ql3bhf7akoo5ikgtshc208md.apps.googleusercontent.com"  # 배포시 보안적용 해야함
    redirect_uri = (
        "http://localhost:8000/accounts/templates/accounts/login/google/callback"
    )
    google_base_url = "https://www.googleapis.com/auth"
    google_email = "/userinfo.email"
    google_myinfo = "/userinfo.profile"
    scope = f"{google_base_url}{google_email}+{google_base_url}{google_myinfo}"
    return redirect(
        f"{google_api}?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}"
    )


def google_callback(request):
    data = {
        "code": request.GET.get("code"),
        "state": request.GET.get("state"),
        "grant_type": "authorization_code",
        "client_id": "526851643558-otkt8p42ql3bhf7akoo5ikgtshc208md.apps.googleusercontent.com",  # 배포시 보안적용 해야함
        "client_secret": "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",
        "redirect_uri": "http://localhost:8000/accounts/templates/accounts/login/google/callback",
    }
    google_token_request_url = "https://oauth2.googleapis.com/token"
    access_token = requests.post(google_token_request_url, data=data).json()[
        "access_token"
    ]
    params = {
        "access_token": f"{access_token}",
    }
    google_call_user_api = "https://www.googleapis.com/oauth2/v3/userinfo"
    google_user_information = requests.get(google_call_user_api, params=params).json()

    g_id = google_user_information["sub"]
    g_name = google_user_information["name"]
    g_email = google_user_information["email"]
    g_img = google_user_information["picture"]

    if get_user_model().objects.filter(google_id=g_id).exists():
        google_user = get_user_model().objects.get(google_id=g_id)
    else:
        google_login_user = get_user_model()()
        google_login_user.username = g_name + g_id
        google_login_user.email = g_email
        google_login_user.google_id = g_id
        google_login_user.image = g_img
        google_login_user.is_social = 1
        google_login_user.set_password(str(state_token))
        google_login_user.save()
        google_user = get_user_model().objects.get(google_id=g_id)
    auth_login(request, google_user)
    return redirect(request.GET.get("next") or "communities:index")
