from django.urls import path
from . import views

app_name = "dogwalking"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:dogwalking_pk>/", views.detail, name="detail"),
    path("<int:dogwalking_pk>/update/", views.update, name="update"),
    path("<int:dogwalking_pk>/delete/", views.delete, name="delete"),
    path("<int:dogwalking_pk>/writing/", views.writing, name="writing"),
    path("walking/<int:dogwalking_pk>/", views.walking, name="walking"),
    # tag
    path("tag/", views.TagCloudTV.as_view(), name="tag_cloud"),
    path("tag/<str:tag>/", views.TaggedObjectLV.as_view(), name="tagged_object_list"),
    # comment
    path(
        "<int:dogwalking_pk>/comment/create/",
        views.comment_create,
        name="comment_create",
    ),
    path(
        "<int:dogwalking_pk>/comment/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    # like
    path("<int:dogwalking_pk>/like/", views.like, name="like"),
    # 리뷰
    path("<int:pk>/review/", views.review, name="review"),
    path(
        "<int:dogwalking_pk>/review/<int:review_pk>/update/",
        views.review_update,
        name="review_update",
    ),
    path(
        "<int:dogwalking_pk>/review/<int:review_pk>/delete/",
        views.review_delete,
        name="review_delete",
    ),
]
