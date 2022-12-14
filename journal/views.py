from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import DailyJournalForm, DogwalkingJournalForm, HealthJournalForm
from accounts.models import Pet

# Create your views here.


# 목록
def journal_list(request, user_pk):
    user = User.objects.get(pk=user_pk)
    daily_journal = user.dailyjournal_set.all()
    dw_journal = user.dogwalkingjournal_set.all()
    health_journal = user.healthjournal_set.all()
    context = {
        "daily_journal": daily_journal,
        "dw_journal": dw_journal,
        "health_journal": health_journal,
        "user": user,
    }
    return render(request, "journal/journal_list.html", context)


# 일기 작성
def daily_create(request):
    if request.method == "POST":
        form = DailyJournalForm(request.POST, request.FILES)
        pet = Pet.objects.get(pk=request.POST.get("pet"))
        if form.is_valid():
            daily = form.save(commit=False)
            daily.user = request.user
            daily.pet = pet
            daily.save()
            return redirect("journal:daily_detail", daily.pk)
    else:
        form = DailyJournalForm()
    context = {
        "form": form,
        "category": "일기",
    }
    return render(request, "journal/daily_create.html", context)


# 일기 조회
def daily_detail(request, dj_pk):
    daily = get_object_or_404(DailyJournal, pk=dj_pk)
    context = {
        "daily": daily,
        "category": "일기",
    }
    return render(request, "journal/daily_detail.html", context)


# 일기 수정
def daily_update(request, dj_pk):
    daily = get_object_or_404(DailyJournal, pk=dj_pk)
    if request.method == "POST":
        form = DailyJournalForm(request.POST, request.FILES, instance=daily)
        if form.is_valid():
            form.save()
            return redirect("journal:daily_detail", daily.pk)
    else:
        form = DailyJournalForm(instance=daily)
    context = {
        "form": form,
        "category": "일기",
        "daily": daily,
    }
    return render(request, "journal/daily_update.html", context)


# 일기 삭제
def daily_delete(request, dj_pk):
    daily_journal = get_object_or_404(DailyJournal, pk=dj_pk)
    daily_journal.delete()
    return redirect("journal:journal_list")


# 산책일기 작성
def dwj_create(request):
    if request.method == "POST":
        form = DogwalkingJournalForm(request.POST, request.FILES)
        pet = Pet.objects.get(pk=request.POST.get("pet"))
        if form.is_valid():
            dwj = form.save(commit=False)
            dwj.user = request.user
            dwj.pet = pet
            dwj.save()
            return redirect("journal:dwj_detail", dwj.pk)
    else:
        form = DogwalkingJournalForm()
    context = {
        "form": form,
        "category": "산책일기",
    }
    return render(request, "journal/dwj_create.html", context)


# 산책일기 조회
def dwj_detail(request, dwj_pk):
    dwj = get_object_or_404(DogwalkingJournal, pk=dwj_pk)
    context = {
        "dwj": dwj,
        "category": "산책 일기",
    }
    return render(request, "journal/dwj_detail.html", context)


# 산책일기 수정
def dwj_update(request, dwj_pk):
    dwj = get_object_or_404(DogwalkingJournal, pk=dwj_pk)
    if request.method == "POST":
        form = DogwalkingJournalForm(request.POST, request.FILES, instance=dwj)
        if form.is_valid():
            form.save()
            return redirect("journal:dwj_detail", dwj.pk)
    else:
        form = DogwalkingJournalForm(instance=dwj)
    context = {
        "form": form,
        "category": "산책 일기",
        "dwj": dwj,
    }
    return render(request, "journal/dwj_update.html", context)


# 산책일기 삭제
def dwj_delete(request, dwj_pk):
    dwj_journal = get_object_or_404(DogwalkingJournal, pk=dwj_pk)
    dwj_journal.delete()
    return redirect("journal:journal_list")


# 건강일기 작성
def health_create(request):
    if request.method == "POST":
        form = HealthJournalForm(request.POST, request.FILES)
        pet = Pet.objects.get(pk=request.POST.get("pet"))
        if form.is_valid():
            health = form.save(commit=False)
            health.user = request.user
            health.pet = pet
            health.save()
            return redirect("journal:health_detail", health.pk)
    else:
        form = HealthJournalForm()
    context = {
        "form": form,
        "category": "건강일기",
    }
    return render(request, "journal/health_create.html", context)


# 건강일기 조회
def health_detail(request, hj_pk):
    health = get_object_or_404(HealthJournal, pk=hj_pk)
    context = {
        "health": health,
        "category": "건강 일기",
    }
    return render(request, "journal/health_detail.html", context)


# 건강일기 수정
def health_update(request, hj_pk):
    health = get_object_or_404(HealthJournal, pk=hj_pk)
    if request.method == "POST":
        form = HealthJournalForm(request.POST, request.FILES, instance=health)
        if form.is_valid():
            form.save()
            return redirect("journal:health_detail", health.pk)
    else:
        form = HealthJournalForm(instance=health)
    context = {
        "form": form,
        "category": "건강 일기",
        "health": health,
    }
    return render(request, "journal/health_update.html", context)


# 건강일기 삭제
def health_delete(request, hj_pk):
    health_journal = get_object_or_404(HealthJournal, pk=hj_pk)
    health_journal.delete()
    return redirect("journal:journal_list")
