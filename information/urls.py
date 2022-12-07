from django.urls import path
from . import views

app_name = "information"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.friends, name="friends"),
]
