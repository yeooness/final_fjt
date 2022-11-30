from . import views
from django.urls import path

app_name = "communities"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:community_pk>/", views.detail, name="detail"),
    path("<int:community_pk>/update/", views.update, name="update"),
    path("<int:community_pk>/delete/", views.delete, name="delete"),
    path("<int:community_pk>/like/", views.like, name="like"),
    # comment
    path(
        "<int:community_pk>/comment/create/",
        views.comment_create,
        name="comment_create",
    ),
    path(
        "<int:community_pk>/comment/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    # tag
    path("tag/", views.TagCloudTV.as_view(), name="tag_cloud"),
    path(
        "tag/<str:tag>/",
        views.TaggedObjectLV.as_view(),
        name="tagged_object_list",
    ),
    path("search/", views.SearchFormView.as_view(), name="search"),
]
