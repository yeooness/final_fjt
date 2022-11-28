from . import views
from django.urls import path

app_name = "community"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:community_pk>/", views.detail, name="detail"),
]
