from django.shortcuts import render, redirect
from .models import Dogwalking
from .forms import DogwalkingForm
from django.views.generic import ListView, TemplateView

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
    context = {
        "dogwalking": dogwalking,
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
