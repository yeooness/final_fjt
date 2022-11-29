from . import views
from django.urls import path

app_name = "communities"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:community_pk>/", views.detail, name="detail"),
    path("<int:community_pk>/update", views.update, name="update"),
    path("<int:community_pk>/delete", views.delete, name="delete"),
]
