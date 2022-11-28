from django.shortcuts import render, redirect
from .models import Dogwalking
from .forms import DogwalkingForm

# Create your views here.
def index(request):
    dogwalking = Dogwalking.objects.order_by("-pk")
    context = {
        "dogwalking": dogwalking,
    }
    return render(request, "dogwalking/index.html", context)


def create(request):
    if request.method == "POST":
        dogwalking_form = DogwalkingForm(request.POST)
        if dogwalking_form.is_valid():
            dogwalking_form.save()
            return redirect("dogwalking:index")
    else:
        dogwalking_form = DogwalkingForm()
    context = {
        "dogwalking_form": dogwalking_form,
    }
    return render(request, "dogwalking/create.html", context)


def detail(request, pk):
    dogwalking = Dogwalking.objects.get(pk=pk)
    context = {
        "dogwalking": dogwalking,
    }
    return render(request, "dogwalking/detail.html")


def update(request, pk):
    dogwalking = Dogwalking.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 가져와서 검증하고 DB 에 저장
        dogwalking_form = DogwalkingForm(request.POST, instance=dogwalking)
        if dogwalking_form.is_valid():
            # 유효성 검사 통과하면 저장후 상세보기 페이지로
            dogwalking_form.save()
            return redirect("dogwalking:detail", dogwalking.pk)
        # 유효성 검사 통과 못하면 => 오류메세지
    else:
        # GET 처리 : Form 을 제공
        dogwalking_form = DogwalkingForm(instance=dogwalking)
    context = {
        "dogwalking_form": dogwalking_form,
    }
    return render(request, "dogwalking/detail.html", context)


def delete(request, pk):
    Dogwalking.objects.get(pk=pk).delete()
    return render(request, "dogwalking/detail.html")
