from django.shortcuts import render, redirect
from .models import DailyJournal, DogwalkingJournal, HealthJournal
from .forms import DailyJournalForm, DogwalkingJournalForm, HealthJournalForm

# Create your views here.


# 목록
def index(request):
    daily_journal = DailyJournal.objects.get("-created_at")
    dog_walking_journal = DogwalkingJournal.objects.get("-created_at")
    health_journal = HealthJournal.objects.get("-created_at")
    context = {
        "daily_journal": daily_journal,
        "dog_walking_journal": dog_walking_journal,
        "health_journal": health_journal,
    }
    render(request, "journal/index.html", context)


# 일기 작성
def daily_create(request):
    if request.method == "POST":
        form = DailyJournalForm(request.POST, request.FILES)
        if form.is_valid():
            daily = form.save(commit=False)
            daily.user = request.user
            daily.save()
            pk = request.user.pk
            return redirect("accounts:detail", pk)
    else:
        form = DailyJournalForm()
    context = {"form": form}
    return render(request, "journal/daily_create.html", context)


# 산책일기 작성
def dwj_create(request):
    if request.method == "POST":
        form = DogwalkingJournalForm(request.POST, request.FILES)
        if form.is_valid():
            dwj = form.save(commit=False)
            dwj.user = request.user
            dwj.save()
            pk = request.user.pk
            return redirect("accounts:detail", pk)
    else:
        form = DogwalkingJournalForm()
    context = {"form": form}
    return render(request, "journal/dwj_create.html", context)


# 건강일기 작성
def health_create(request):
    if request.method == "POST":
        form = HealthJournalForm(request.POST, request.FILES)
        if form.is_valid():
            health = form.save(commit=False)
            health.user = request.user
            health.save()
            pk = request.user.pk
            return redirect("accounts:detail", pk)
    else:
        form = HealthJournalForm()
    context = {"form": form}
    return render(request, "journal/health_create.html", context)
