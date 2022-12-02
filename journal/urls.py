from django.urls import path
from . import views

app_name = "journal"

urlpatterns = [
    # 목록
    path("journal_list/", views.journal_list, name="journal_list"),
    # 일기 CRUD
    path("daily_journal/create/", views.daily_create, name="daily_create"),
    path("daily_journal/<int:dj_pk>/", views.daily_detail, name="daily_detail"),
    path(
        "daily_journal/update/<int:dj_pk>/",
        views.daily_update,
        name="daily_update",
    ),
    path(
        "daily_journal/delete/<int:dj_pk>/",
        views.daily_delete,
        name="daily_delete",
    ),
    # 산책 일지 CRUD
    path("dw_journal/create/", views.dwj_create, name="dwj_create"),
    path("dw_journal/<int:dwj_pk>/", views.dwj_detail, name="dwj_detail"),
    path("dw_journal/update/<int:dwj_pk>/", views.dwj_update, name="dwj_update"),
    path("dw_journal/delete/<int:dwj_pk>/", views.dwj_delete, name="dwj_delete"),
    # 건강일지 CRUD
    path("health_journal/create/", views.health_create, name="health_create"),
    path("health_journal/<int:hj_pk>/", views.health_detail, name="health_detail"),
    path(
        "health_journal/update/<int:hj_pk>/",
        views.health_update,
        name="health_update",
    ),
    path(
        "health_journal/delete/<int:hj_pk>/",
        views.health_delete,
        name="health_delete",
    ),
]
