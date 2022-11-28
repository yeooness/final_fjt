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
]
