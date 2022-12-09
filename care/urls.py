from django.urls import path
from . import views

app_name = "care"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:care_pk>/", views.detail, name="detail"),
    path("<int:care_pk>/update/", views.update, name="update"),
    path("<int:care_pk>/delete/", views.delete, name="delete"),
    # like
    path("<int:care_pk>/like/", views.like, name="like"),
    # comment
    path(
        "<int:care_pk>/comment/create/",
        views.comment_create,
        name="comment_create",
    ),
    path(
        "<int:care_pk>/comment/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    # 리뷰
    path("<int:pk>/review/", views.review, name="review"),
    path(
        "<int:care_pk>/review/<int:review_pk>/update/",
        views.review_update,
        name="review_update",
    ),
    path(
        "<int:care_pk>/review/<int:review_pk>/delete/",
        views.review_delete,
        name="review_delete",
    ),
]
