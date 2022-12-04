from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # 회원가입
    path("signup/", views.signup, name="signup"),
    # 로그인
    path("login/", views.login, name="login"),
    # 로그아웃
    path("logout/", views.logout, name="logout"),
    # 프로필 페이지
    path("<int:user_pk>/", views.detail, name="detail"),
    # 프로필 수정
    path("<int:user_pk>/update/", views.update, name="update"),
    # 비밀번호 변경
    path("<int:user_pk>/passwordchange/", views.passwordchange, name="passwordchange"),
    # 회원 탈퇴
    path("delete/", views.delete, name="delete"),
    # 반려동물 등록
    path("<int:user_pk>/pet_register/", views.pet_register, name="pet_register"),
    # 반려동물 정보 페이지
    path("<int:user_pk>/<int:pet_pk>/pet_detail/", views.pet_detail, name="pet_detail"),
    # 반려동물 정보 수정
    path("<int:user_pk>/<int:pet_pk>/pet_update/", views.pet_update, name="pet_update"),
    # 팔로우
    path("<int:user_pk>/follow/", views.follow, name="follow"),
    # 차단
    path("<int:user_pk>/block/", views.block, name="block"),
    path("block_user/", views.block_user, name="block_user"),
    path(
        "<int:user_pk>/block_user_block/",
        views.block_user_block,
        name="block_user_block",
    ),
    # 카카오 로그인
    path("login/kakao", views.kakao_request, name="kakao"),
    path("templates/accounts/login/kakao/callback", views.kakao_callback),
    # 네이버 로그인
    path("login/naver", views.naver_request, name="naver"),
    path("templates/accounts/login/naver/callback", views.naver_callback),
    # 구글 로그인
    path("login/google", views.google_request, name="google"),
    path("templates/accounts/login/google/callback", views.google_callback),
    # 핸드폰 인증
    path("<int:user_pk>/phone_auth/", views.phone_auth, name="phone_auth"),
    path("<int:user_pk>/check_auth/", views.check_auth, name="check_auth"),
]
