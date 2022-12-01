from django.shortcuts import render, redirect, get_object_or_404
from .models import Care, Comment
from .forms import Careform, CommentForm

# from django.views.generic import ListView, TemplateView
from django.http import JsonResponse

# Create your views here.
def index(request):
    care = Care.objects.order_by("-pk")
    context = {
        "care": care,
    }
    return render(request, "care/index.html", context)


def create(request):
    if request.method == "POST":
        # tags = request.POST.get("tags", "").split(",")
        care_form = Careform(request.POST, request.FILES)
        if care_form.is_valid():
            care = care_form.save(commit=False)
            care.user = request.user
            care.save()
            # for tag in tags:
            #     tag = tag.strip()
            #     if tag != "":
            #         dogwalking.tags.add(tag)
            return redirect("care:index")
    else:
        care_form = Careform()
    context = {
        "care_form": care_form,
    }
    return render(request, "care/create.html", context)


def detail(request, care_pk):
    care = Care.objects.get(pk=care_pk)
    form = CommentForm()
    context = {
        "care": care,
        "comments": care.comment_set.all(),
        "form": form,
    }
    return render(request, "care/detail.html", context)


def update(request, care_pk):
    care = Care.objects.get(pk=care_pk)
    if request.user == care.user:
        if request.method == "POST":
            care_form = Careform(request.POST, request.FILES, instance=care)

            if care_form.is_valid():
                care_form.save()
                return redirect("care:detail", care_pk)
        else:
            care_form = Careform(instance=care)

        return render(
            request,
            "care/update.html",
            {
                "care_form": care_form,
            },
        )
    else:
        return redirect(request, "care/update.html", care_pk)


def delete(request, care_pk):
    Care.objects.get(pk=care_pk).delete()
    return redirect("care:index")


# def comment_create(request, pk):
#     dogwalking = Dogwalking.objects.get(pk=pk)
#     comment_form = CommentForm(request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.dogwalking = dogwalking
#         comment.user = request.user
#         comment.save()
#     return redirect("dogwalking:detail", dogwalking.pk)


# def comment_delete(request, dogwalking_pk, comment_pk):
#     dogwalking = Dogwalking.objects.get(pk=comment_pk)
#     if request.user == dogwalking.user:
#         dogwalking.delete()
#     return redirect("dogwalking:detail", dogwalking_pk)


def like(request, care_pk):
    care = get_object_or_404(Care, pk=care_pk)
    if request.user in care.like_user.all():
        care.like_user.remove(request.user)
        is_liked = False
    else:
        care.like_user.add(request.user)
        is_liked = True
    context = {"is_liked": is_liked, "likeCount": care.like_user.count()}
    return JsonResponse(context)


# 댓글
def comment_create(request, care_pk):
    care_data = Care.objects.get(pk=care_pk)

    if request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.care = care_data
            comment.user = request.user
            comment.save()
        return redirect("care:detail", care_pk)
    return redirect("accounts:login")


def comment_delete(request, care_pk, comment_pk):
    comment_data = Comment.objects.get(pk=comment_pk)

    if request.user == comment_data.user:
        comment_data.delete()
    return redirect("care:detail", care_pk)
