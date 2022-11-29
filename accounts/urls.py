from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 회원가입
    path('signup/', views.signup, name='signup'),
    # 로그인
    path('login/', views.login, name='login'),
    # 로그아웃
    path('logout/', views.logout, name='logout'),
    # 프로필 페이지
    path('<int:user_pk>/', views.detail, name='detail'),
    # 프로필 수정
    path('<int:user_pk>/update/', views.update, name='update'),
    # 비밀번호 변경
    path('<int:user_pk>/passwordchange/', views.passwordchange, name='passwordchange'),
    # 회원 탈퇴
    path('<int:user_pk>/delete/', views.delete, name='delete'),

    # 카카오 로그인
    path('login/kakao/', views.kakao_request, name='kakao'),
    path('templates/accounts/login/kakao/callback', views.kakao_callback),
    # 네이버 로그인
    path('login/naver/', views.naver_request, name='naver'),
    path('login/naver/callback/', views.naver_callback),
    # 구글 로그인
    path('login/google/', views.google_request, name='google'),
    path('templates/accounts/login/google/callback', views.google_callback),
]
