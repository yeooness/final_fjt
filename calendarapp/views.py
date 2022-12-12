from datetime import datetime, date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta
import calendar
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import *
from .utils import Calendar
from .forms import *

# Create your views here.
def index(request):
    return HttpResponse("hello")


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month


class CalendarView(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = "calendarapp/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context


def create_daily_event(request):
    form = DailyEventForm(request.POST or None)
    # pet = Pet.objects.get(pk=request.POST.get("pet"))
    if request.POST and form.is_valid():
        content = form.cleaned_data["content"]
        start_time = form.cleaned_data["start_time"]
        pet = form.data["pet"]
        Event.objects.get_or_create(
            content=content,
            start_time=start_time,
            pet=pet,
        )
        form.save()
        return HttpResponseRedirect(reverse("calendarapp:calendar"))
    return render(request, "calendarapp/event.html", {"form": form})


def create_dogwalking_event(request):
    form = DogwalkingEventForm(request.POST or None)
    if request.POST and form.is_valid():
        route = form.cleaned_data["route"]
        consumed_calories = form.cleaned_data["consumed_calories"]
        walking_time = form.cleaned_data["walking_time"]
        start_time = form.cleaned_data["start_time"]
        # end_time = form.cleaned_data["end_time"]
        Dogwalking_Journal.objects.get_or_create(
            user=request.user,
            route=route,
            consumed_calories=consumed_calories,
            walking_time=walking_time,
            start_time=start_time,
            # end_time=end_time,
        )
        return HttpResponseRedirect(reverse("calendarapp:calendar"))
    return render(request, "calendarapp/event.html", {"form": form})


def create_health_event(request):
    form = HealthEventForm(request.POST or None)
    if request.POST and form.is_valid():
        meals = form.cleaned_data["meals"]
        energy = form.cleaned_data["energy"]
        medicine = form.changed_data["medicine"]
        start_time = form.cleaned_data["start_time"]
        # end_time = form.cleaned_data["end_time"]
        Event.objects.get_or_create(
            user=request.user,
            meals=meals,
            energy=energy,
            medicine=medicine,
            start_time=start_time,
            # end_time=end_time,
        )
        return HttpResponseRedirect(reverse("calendarapp:calendar"))
    return render(request, "calendarapp/event.html", {"form": form})


# 산책일지
def create_dogwalking(request):
    form = DogwalkingJournalForm(request.POST or None)
    if request.POST and form.is_valid():
        route = form.cleaned_data["route"]
        consumed_calories = form.cleaned_data["consumed_calories"]
        walking_time = form.cleaned_data["walking_time"]
        start_time = form.cleaned_data["start_time"]
        # end_time = form.cleaned_data["end_time"]
        Dogwalking_Journal.objects.get_or_create(
            user=request.user,
            route=route,
            consumed_calories=consumed_calories,
            walking_time=walking_time,
            start_time=start_time,
            # end_time=end_time,
        )
        return HttpResponseRedirect(reverse("calendarapp:calendar"))
    return render(request, "calendarapp/dwj.html", {"form": form})


class EventEdit(generic.UpdateView):
    model = Event
    fields = ["title", "description", "start_time", "end_time"]
    template_name = "calendarapp/event.html"


# @login_required(login_url='signup')
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    # eventmember = EventMember.objects.filter(event=event)
    context = {
        "event": event,
        # "eventmember": eventmember
    }
    return render(request, "calendarapp/event-details.html", context)


def add_eventmember(request, event_id):
    forms = AddMemberForm()
    if request.method == "POST":
        forms = AddMemberForm(request.POST)
        if forms.is_valid():
            member = EventMember.objects.filter(event=event_id)
            event = Event.objects.get(id=event_id)
            if member.count() <= 9:
                user = forms.cleaned_data["user"]
                EventMember.objects.create(event=event, user=user)
                return redirect("calendarapp:calendar")
            else:
                print("--------------User limit exceed!-----------------")
    context = {"form": forms}
    return render(request, "calendarapp/add_member.html", context)


class EventMemberDeleteView(generic.DeleteView):
    model = EventMember
    template_name = "calendarapp/event_delete.html"
    success_url = reverse_lazy("calendarapp:calendar")
