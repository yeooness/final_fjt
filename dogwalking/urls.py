from django.urls import path
from . import views

app_name = "dogwalking"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:dogwakling_pk>/", views.detail, name="detail"),
    path("<int:dogwakling_pk>/update/", views.update, name="update"),
    path("<int:dogwakling_pk>/delete/", views.delete, name="delete"),
    path("tag/", views.TagCloudTV.as_view(), name="tag_cloud"),
    path("tag/<str:tag>/", views.TaggedObjectLV.as_view(), name="tagged_object_list"),
]
