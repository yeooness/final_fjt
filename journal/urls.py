from django.urls import path
from . import views

app_name = "journal"

urlpatterns = [
    # 목록
    path("", views.index, name="index"),
    # 일기 CRUD
    path("journal/daily_journal/create/", views.daily_create, name="daily_create"),
    # path("journal/daily_journal/<int:dj_pk>/", views.daily_detail, name="daily_detail"),
    # path(
    #     "journal/daily_journal/update/<int:dj_pk>/",
    #     views.daily_update,
    #     name="daily_update",
    # ),
    # path(
    #     "journal/daily_journal/delete/<int:dj_pk>/",
    #     views.daily_delete,
    #     name="daily_delete",
    # ),
    # 산책 일지 CRUD
    path("journal/dw_journal/create/", views.dwj_create, name="dwj_create"),
    # path("journal/dw_journal/<int:dwj_pk>/", views.dwj_detail, name="dwj_detail"),
    # path(
    #     "journal/dw_journal/update/<inr:dwj_pk>/", views.dwj_update, name="dwj_update"
    # ),
    # path(
    #     "journal/dw_journal/delete/<int:dwj_pk>/", views.dwj_delete, name="dwj_delete"
    # ),
    # 건강일지 CRUD
    path("journal/health_journal/create/", views.health_create, name="health_create"),
    # path(
    #     "journal/health_journal/<int:hj_pk>/", views.health_detail, name="health_detail"
    # ),
    # path(
    #     "journal/health_journal/update/<int:hj_pk>/",
    #     views.health_update,
    #     name="health_update",
    # ),
    # path(
    #     "journal/health_journal/delete/<int:hj_pk>/",
    #     views.health_delete,
    #     name="health_delete",
    # ),
]
