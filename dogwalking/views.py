from django.shortcuts import render, redirect, get_object_or_404
from .models import Dogwalking
from .forms import DogwalkingForm, CommentForm
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse

# Create your views here.
def index(request):
    dogwalking = Dogwalking.objects.order_by("-pk")
    context = {
        "dogwalking": dogwalking,
    }
    return render(request, "dogwalking/index.html", context)


def create(request):
    if request.method == "POST":
        tags = request.POST.get("tags", "").split(",")
        dogwalking_form = DogwalkingForm(request.POST, request.FILES)
        if dogwalking_form.is_valid():
            dogwalking = dogwalking_form.save(commit=False)
            dogwalking.user = request.user
            dogwalking.save()
            for tag in tags:
                tag = tag.strip()
                if tag != "":
                    dogwalking.tags.add(tag)
            return redirect("dogwalking:index")
    else:
        dogwalking_form = DogwalkingForm()
    context = {
        "dogwalking_form": dogwalking_form,
    }
    return render(request, "dogwalking/create.html", context)


def detail(request, dogwakling_pk):
    dogwalking = Dogwalking.objects.get(pk=dogwakling_pk)
    comment_form = CommentForm()
    context = {
        "dogwalking": dogwalking,
        "comments": dogwalking.comment_set.all(),
        "comment_form": comment_form,
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

        return render(
            request,
            "dogwalking/update.html",
            {
                "dogwalking_form": dogwalking_form,
            },
        )
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


def comment_create(request, pk):
    dogwalking = Dogwalking.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.dogwalking = dogwalking
        comment.user = request.user
        comment.save()
    return redirect("dogwalking:detail", dogwalking.pk)


def comment_delete(request, dogwalking_pk, comment_pk):
    dogwalking = Dogwalking.objects.get(pk=comment_pk)
    if request.user == dogwalking.user:
        dogwalking.delete()
    return redirect("dogwalking:detail", dogwalking_pk)


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
