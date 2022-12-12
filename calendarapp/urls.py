from django.urls import path
from . import views

app_name = "calendarapp"

urlpatterns = [
    path("index", views.index, name="index"),
    path("", views.CalendarView.as_view(), name="calendar"),
    path("event/daily_new/", views.create_daily_event, name="create_daily_event"),
    path(
        "event/dogwalking_new/",
        views.create_dogwalking,
        name="create_dogwalking",
    ),
    path("event/health_new/", views.create_health_event, name="create_health_event"),
    path("event/edit/<int:pk>/", views.EventEdit.as_view(), name="event_edit"),
    path("event/<int:event_id>/details/", views.event_details, name="event-detail"),
    path(
        "add_eventmember/<int:event_id>", views.add_eventmember, name="add_eventmember"
    ),
    path(
        "event/<int:pk>/remove",
        views.EventMemberDeleteView.as_view(),
        name="remove_event",
    ),
    # 산책일지
    path("dogwalking/new/", views.create_dogwalking, name="dogwalking_new"),
]
