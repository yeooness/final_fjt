from django.shortcuts import render, redirect, get_object_or_404
from .models import Dogwalking, Comment, Alarm
from .forms import DogwalkingForm, CommentForm, AlarmForm
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    dogwalking = Dogwalking.objects.order_by("-pk")
    context = {
        "dogwalking": dogwalking,
    }
    return render(request, "dogwalking/index.html", context)


def create(request):
    if request.method == "POST":
        # tags = request.POST.get("tags", "").split(",")
        dogwalking_form = DogwalkingForm(request.POST, request.FILES)
        if dogwalking_form.is_valid():
            dogwalking = dogwalking_form.save(commit=False)
            dogwalking.user = request.user
            dogwalking.save()
            # for tag in tags:
            #     tag = tag.strip()
            #     if tag != "":
            #         dogwalking.tags.add(tag)
            return redirect("dogwalking:detail", dogwalking.pk)
    else:
        dogwalking_form = DogwalkingForm()
    context = {
        "dogwalking_form": dogwalking_form,
    }
    return render(request, "dogwalking/create.html", context)


def detail(request, dogwakling_pk):
    dogwalking = Dogwalking.objects.get(pk=dogwakling_pk)
    comments = dogwalking.comment_set.all()
    form = CommentForm()
    dogwalking.save()
    context = {
        "dogwalking": dogwalking,
        "comments": comments,
        "form": form,
    }
    return render(request, "dogwalking/detail.html", context)


def update(request, dogwakling_pk):
    dogwalking = Dogwalking.objects.get(pk=dogwakling_pk)
    if request.user == dogwalking.user:
        if request.method == "POST":
            dogwalking_form = DogwalkingForm(
                request.POST, request.FILES, instance=dogwalking
            )

            if dogwalking_form.is_valid():
                dogwalking_form.save()
                return redirect("dogwalking:detail", dogwakling_pk)
        else:
            dogwalking_form = DogwalkingForm(instance=dogwalking)

        context = {
            "dogwalking_form": dogwalking_form,
            'dogwalking': dogwalking,
        }

        return render(request, "dogwalking/update.html", context)
    else:
        return redirect(request, "dogwalking/update.html", dogwakling_pk)


def delete(request, dogwakling_pk):
    Dogwalking.objects.get(pk=dogwakling_pk).delete()
    return redirect("dogwalking:index")


class TagCloudTV(TemplateView):
    template_name = "taggit/taggit_cloud.html"


class TaggedObjectLV(ListView):
    template_name = "taggit/taggit_post_list.html"
    model = Dogwalking

    def get_queryset(self):
        return Dogwalking.objects.filter(tags__name=self.kwargs.get("tag"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tagname"] = self.kwargs["tag"]
        return context


def comment_create(request, dogwakling_pk):
    dogwalking_data = Dogwalking.objects.get(pk=dogwakling_pk)

    if request.user.is_authenticated:
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.dogwalking = dogwalking_data
            comment.user = request.user
            comment.save()
    return redirect("dogwalking:detail", dogwakling_pk)


def comment_delete(request, dogwakling_pk, comment_pk):
    comment_data = Comment.objects.get(pk=comment_pk)

    if request.user == comment_data.user:
        comment_data.delete()
    return redirect("dogwalking:detail", dogwakling_pk)


def like(request, dogwalking_pk):
    dogwalking = get_object_or_404(Dogwalking, pk=dogwalking_pk)
    if request.user in dogwalking.like_user.all():
        dogwalking.like_user.remove(request.user)
        is_liked = False
    else:
        dogwalking.like_user.add(request.user)
        is_liked = True
    context = {"is_liked": is_liked, "likeCount": dogwalking.like_user.count()}
    return JsonResponse(context)


# 산책요청
@login_required
def alarm(request):
    alarm = request.user.user_to_dw.order_by("-created_at")
    to_alarm = request.user.user_from_dw.order_by("-created_at")

    return render(
        request,
        "dogwalking/alarm.html",
        {"alarm": alarm, "to_alarm": to_alarm},
    )


@login_required
def send(request, pk):
    alarm = request.user.user_to_dw.order_by("-created_at")
    to_user = get_object_or_404(get_user_model(), pk=pk)
    form = AlarmForm(request.POST or None)
    if form.is_valid():
        temp = form.save(commit=False)
        temp.from_user = request.user
        temp.to_user = to_user
        temp.save()
        if to_user.note_notice:
            to_user.notice_note = False
            to_user.save()
        return redirect("dogwalking:alarm")
    context = {
        "alarm": alarm,
        "form": form,
        "to_user": to_user,
    }
    return render(request, "dogwalking/send.html", context)


def a_detail(request, pk):
    alarm = get_object_or_404(Alarm, pk=pk)

    if request.user == alarm.to_user:
        if not alarm.read:
            alarm.read = True
            alarm.save()
        if not request.user.user_to.filter(read=False).exists():
            request.user.notice_note = True
            request.user.save()
        return render(request, "dogwalking/a_detail.html", {"alarm": alarm})
    elif request.user == alarm.from_user:
        return render(request, "dogwalking/a_detail.html", {"alarm": alarm})
    else:
        return redirect("dogwalking:alarm")


def a_delete(request, pk):
    alarm = get_object_or_404(Alarm, pk=pk)
    print(request.POST)
    if request.user == alarm.to_user and request.method == "POST":
        alarm.delete()
        return JsonResponse({"pk": pk})
    else:
        return redirect("dogwalking:index")
