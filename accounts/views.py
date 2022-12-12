from random import randint
import secrets, requests
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import *
from care.models import *
from .models import Pet, AuthPhone
from .forms import *
from django.contrib.auth import (
    authenticate,
    update_session_auth_hash,
    get_user_model,
    login as auth_login,
    logout as auth_logout,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from datetime import date, datetime
import re

# Create your views here.

# 회원가입
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.postcode = request.POST.get("postcode")
            user.address = request.POST.get("address")
            user.detailAddress = request.POST.get("detailAddress")
            user.extraAddress = request.POST.get("extraAddress")
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
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("communities:index")
    else:
        form = CustomAuthenticationForm()
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
    # 차단 목록
    user_blocks = user.block.order_by("pk")
    context = {
        "user": user,
        "user_pets": user_pets,
        # 'user_boards' : user_boards,
        # 'user_reviews' : user_reviews,
        "user_followers": user_followers,
        "user_followings": user_followings,
        "user_blocks": user_blocks,
        "all_pet": Pet.objects.all(),
    }
    return render(request, "accounts/detail.html", context)


# 반려동물 등록
def pet_register(request, user_pk):
    if request.method == "POST":
        form = CustomPetCreationForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.species = request.POST.get("pet_species")
            # pet.size = request.POST.get("pet_size")
            # pet.weight = request.POST.get("weight")
            pet.petgender = request.POST.get("pet_gender")
            pet.neutralization = request.POST.get("pet_neutralization")
            pet.vaccination_status = request.POST.get("pet_vaccination")
            pet.characteristics = request.POST.getlist("feature")

            today = datetime.datetime.now().date()
            birthday = date.fromisoformat(request.POST.get("birthday"))
            pet.petage = int((today - birthday).days / 365.25)
            # if pet.feature:
            #     query = Q()
            #     for i in pet.feature:
            #         query = query | Q(feature__icontains=i)
            #         pet = pet.filter(query)
            pet.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomPetCreationForm()
    context = {"form": form}
    return render(request, "accounts/pet_register.html", context)


# 반려동물 정보 페이지
def pet_detail(request, user_pk, pet_pk):
    pet = get_object_or_404(Pet, pk=pet_pk)
    p = re.compile("[가-힣]+")
    features = p.findall(pet.characteristics)
    context = {
        "pet": pet,
        "features": features,
    }
    return render(request, "accounts/pet_detail.html", context)


# 반려동물 정보 수정
def pet_update(request, user_pk, pet_pk):
    pet = get_object_or_404(Pet, pk=pet_pk)
    if request.method == "POST":
        form = CustomPetChangeForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            print(request.POST.getlist("feature"))
            pet = form.save(commit=False)
            pet.user = request.user
            pet.species = request.POST.get("pet_species")
            # pet.size = request.POST.get("pet_size")
            # pet.pet_weight = request.POST.get("pet_weight")
            pet.petgender = request.POST.get("pet_gender")
            pet.neutralization = request.POST.get("pet_neutralization")
            pet.vaccination_status = request.POST.get("pet_vaccination")
            pet.characteristics = request.POST.getlist("feature")

            today = datetime.datetime.now().date()
            birthday = date.fromisoformat(request.POST.get("birthday"))
            pet.petage = int((today - birthday).days / 365.25)
            pet.save()
            return redirect("accounts:pet_detail", request.user.pk, pet.pk)
    else:
        form = CustomPetChangeForm(instance=pet)
        print(form)

    context = {
        "form": form,
        "pet": pet,
    }
    return render(request, "accounts/pet_update.html", context)


# 반려동물 등록 삭제
def pet_delete(request, user_pk, pet_pk):
    pet = get_object_or_404(Pet, pk=pet_pk)
    pet.delete()
    return redirect("accounts:detail", user_pk)


# 회원 정보 수정
@login_required
def update(request, user_pk):
    if request.user.pk == user_pk:
        user = get_object_or_404(get_user_model(), pk=user_pk)
        if request.method == "POST":
            update_form = CustomUserChangeForm(
                request.POST, request.FILES, instance=request.user
            )
            auth_form = AuthForm(request.POST, instance=user)
            if update_form.is_valid() and auth_form.is_valid():
                user = update_form.save(commit=False)
                user.postcode = request.POST.get("postcode")
                user.address = request.POST.get("address")
                user.detailAddress = request.POST.get("detailAddress")
                user.extraAddress = request.POST.get("extraAddress")
                auth_form.save()
                user.save()
                return redirect("accounts:detail", user_pk)
        else:
            update_form = CustomUserChangeForm(instance=request.user)
            auth_form = AuthForm(instance=user)
        context = {"update_form": update_form, "auth_form": auth_form}
        return render(request, "accounts/update.html", context)
    else:
        return redirect("communities:index")


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
    redirect_uri = "http://danggeunjibsabean-env.eba-z2wmzac2.ap-northeast-2.elasticbeanstalk.com/accounts/templates/accounts/login/kakao/callback"
    client_id = "3044dd3e42caed2e8e6ed2f4650c22f7"  # 배포시 보안적용 해야함
    return redirect(f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}")


def kakao_callback(request):
    data = {
        "grant_type": "authorization_code",
        "client_id": "3044dd3e42caed2e8e6ed2f4650c22f7",  # 배포시 보안적용 해야함
        "redirect_uri": "http://danggeunjibsabean-env.eba-z2wmzac2.ap-northeast-2.elasticbeanstalk.com/accounts/templates/accounts/login/kakao/callback",
        "code": request.GET.get("code"),
    }
    kakao_token_api = "https://kauth.kakao.com/oauth/token"
    access_token = requests.post(kakao_token_api, data=data).json()["access_token"]

    headers = {"Authorization": f"bearer ${access_token}"}
    kakao_user_api = "https://kapi.kakao.com/v2/user/me"
    kakao_user_information = requests.get(kakao_user_api, headers=headers).json()

    kakao_id = kakao_user_information["id"]
    kakao_nickname = kakao_user_information["properties"]["nickname"]

    if get_user_model().objects.filter(kakao_id=kakao_id).exists():
        kakao_user = get_user_model().objects.get(kakao_id=kakao_id)
    else:
        kakao_login_user = get_user_model()()
        kakao_login_user.username = kakao_id
        kakao_login_user.nickname = kakao_id
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
    redirect_uri = "http://danggeunjibsabean-env.eba-z2wmzac2.ap-northeast-2.elasticbeanstalk.com/accounts/templates/accounts/login/naver/callback"
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
        "redirect_uri": "http://danggeunjibsabean-env.eba-z2wmzac2.ap-northeast-2.elasticbeanstalk.com/accounts/templates/accounts/login/naver/callback",
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
    if get_user_model().objects.filter(naver_id=naver_id).exists():
        naver_user = get_user_model().objects.get(naver_id=naver_id)
    else:
        naver_login_user = get_user_model()()
        naver_login_user.username = naver_id
        naver_login_user.nickname = naver_nickname
        naver_login_user.naver_id = naver_id
        naver_login_user.set_password(str(state_token))
        naver_login_user.is_social = 2
        naver_login_user.save()
        naver_user = get_user_model().objects.get(naver_id=naver_id)
    auth_login(request, naver_user)
    return redirect(request.GET.get("next") or "communities:index")


# 구글 로그인
def google_request(request):
    google_api = "https://accounts.google.com/o/oauth2/v2/auth"
    client_id = "526851643558-otkt8p42ql3bhf7akoo5ikgtshc208md.apps.googleusercontent.com"  # 배포시 보안적용 해야함
    redirect_uri = "http://danggeunjibsabean-env.eba-z2wmzac2.ap-northeast-2.elasticbeanstalk.com/accounts/templates/accounts/login/google/callback"
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
        "redirect_uri": "http://danggeunjibsabean-env.eba-z2wmzac2.ap-northeast-2.elasticbeanstalk.com/accounts/templates/accounts/login/google/callback",
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

    if get_user_model().objects.filter(google_id=g_id).exists():
        google_user = get_user_model().objects.get(google_id=g_id)
    else:
        google_login_user = get_user_model()()
        google_login_user.username = g_id
        google_login_user.nickname = g_email
        google_login_user.email = g_email
        google_login_user.google_id = g_id
        google_login_user.is_social = 1
        google_login_user.set_password(str(state_token))
        google_login_user.save()
        google_user = get_user_model().objects.get(google_id=g_id)
    auth_login(request, google_user)
    return redirect(request.GET.get("next") or "communities:index")


# 핸드폰 인증
import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models as m


def check(request, user_pk):
    today_ = str(datetime.date.today())
    user = get_object_or_404(get_user_model(), pk=user_pk)
    user_phone = request.POST["phone"]
    now_auth_phone = AuthPhone.objects.filter(phone=user_phone[1:])
    auth_count = 0
    for data in now_auth_phone:
        if data.created_at.strftime("%Y-%m-%d") == today_:
            auth_count += 1
            if auth_count == 5:
                break
    context = {
        "authCount": auth_count,
    }
    return JsonResponse(context)


# 휴대폰 인증번호 전송
def phone_auth(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if user.phone_num:
        phone = user.phone_num
        phone = "".join(phone.split("-"))
        user.phone_num = phone
    random_auth_number = randint(1000, 10000)
    auth_phone = AuthPhone()
    auth_phone.phone = user.phone_num if user.phone_num else request.POST["phone"]
    print(user.phone_num)
    print(request.POST["phone"])
    auth_phone.auth_number = random_auth_number
    auth_phone.save()
    context = {}
    return JsonResponse(context)


import datetime
from django.utils import timezone


# 휴대폰 인증번호 입력 후 검증
def check_auth(request, user_pk):
    time_limit = timezone.now() + datetime.timedelta(minutes=5)
    user_phone = request.POST["phone"]
    phone_auth_number = int(request.POST["auth_number"])
    user = get_object_or_404(get_user_model(), pk=user_pk)
    now_auth_phone = AuthPhone.objects.filter(phone=user_phone[1:]).order_by(
        "-updated_at"
    )[0]
    if now_auth_phone.updated_at <= time_limit:
        if now_auth_phone.auth_number == phone_auth_number:
            user.phone = user_phone
            user.is_phone_active = True
            user.save()
            now_auth_phone.delete()
            is_phone_active = True
            auth_error_or_success = "인증 완료"
        else:
            is_phone_active = False
            auth_error_or_success = "인증 번호가 다릅니다."
    else:
        is_phone_active = False
        auth_error_or_success = "인증 시간이 만료되었습니다."
    context = {
        "isPhoneActive": is_phone_active,
        "authErrorOrSuccess": auth_error_or_success,
    }
    return JsonResponse(context)


# 알람
def notice(request):
    if request.method == "POST":
        dic = {}
        if request.user.note_notice:
            if request.user.user_to.filter(read=False).exists():
                false_notes = request.user.user_to.filter(read=False)
                for i in false_notes:
                    if i.created_at not in dic:
                        dic[i.created_at.strftime("%Y-%m-%dT%H:%M:%S")] = (
                            i.title,
                            i.from_user.nickname,
                            "note",
                            i.pk,
                        )
                    else:
                        dic[
                            (i.created_at + datetime.timedelta(minutes=1)).strftime(
                                "%Y-%m-%dT%H:%M:%S"
                            )
                        ] = (i.title, i.from_user.nickname, "note", i.pk)
        dic = sorted(dic.items(), reverse=True)
        if not dic:
            request.user.notice_pet = True
            request.user.notice_note = True
            request.user.save()
        return JsonResponse({"items": dic})
    else:
        return redirect("communities:index")
