from django.urls import path

from . import views

app_name = "schedule"

urlpatterns = [
    # GET : /schedule/
    path("", views.index, name="index"),
    # GET : /schedule/get_events/
    path("get_events/", views.get_events, name="get_events"),
    # POST : /schedule/set_all_day_event/ - { title: "이벤트1", start: "2021-11-04", end: "2021-11-05", allDay=True }
    path("set_all_day_event/", views.set_all_day_event, name="set_all_day_event"),
]
