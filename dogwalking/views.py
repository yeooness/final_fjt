from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Pet
from .models import Dogwalking, Comment, Review
from .forms import DogwalkingForm, CommentForm, ReviewForm
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from datetime import date
from django.db.models import Q

# Create your views here.
def index(request):
    pet = Pet.objects.all()
    dogwalking = Dogwalking.objects.order_by("-pk")
    pet_species = request.GET.getlist('pet_species') # 견종
    dog_size = request.GET.getlist('dog_size') # 강아지 크기
    dog_personality = request.GET.getlist('dog_personality') # 강아지 성격
    cat_size = request.GET.getlist('cat_size') # 고양이 크기
    cat_personality = request.GET.getlist('cat_personality') # 고양이 성격
    area = request.GET.get('area')

    # 매칭

    # 견종
    pet_species_list = ['강아지', '고양이']
    #강아지 크기별
    dog_size_list = ['대형견', '중형견', '소형견']
    # 강아지 성격별
    dog_personality_list = ['활발한', '소심한', '긍정적인', '적응력높은', '충성심높은', '공격적인', '애교많은']
    # 고양이 크기별
    cat_size_list = ['대형묘', '중형묘', '소형묘']
    # 고양이 성격별
    cat_personality_list = ['예민한', '공격적인', '애교많은', '호기심많은', '겁이많은']

    # DB모델
    if pet_species:
        query = Q()
        for i in pet_species:
            query = query | Q(pet_species__icontains=i)
            dogwalking = dogwalking.filter(query)
    if dog_size:
        query = Q()
        for i in dog_size:
            query = query | Q(dog_size__icontains=i)
            dogwalking = dogwalking.filter(query)
    if dog_personality:
        query = Q()
        for i in  dog_personality:
            query = query | Q(dog_personality__icontains=i)
            dogwalking = dogwalking.filter(query)
    if cat_size:
        query = Q()
        for i in cat_size:
            query = query | Q(cat_size__icontains=i)
            dogwalking = dogwalking.filter(query)
    if cat_personality:
        query = Q()
        for i in cat_personality:
            query = query | Q(cat_personality__icontains=i)
            dogwalking = dogwalking.filter(query)
    if area:
        query = Q()
        for i in area:
            query = query | Q(area__icontains=i)
            dogwalking = dogwalking.filter(query)


    context = {
        "pet":pet,
        "dogwalking": dogwalking,
        "dog_size": dog_size,
        "dog_personality": dog_personality,
        "cat_size": cat_size,
        "cat_personality": cat_personality,
        "area": area,
        "pet_species_list": pet_species_list,
        "dog_size_list": dog_size_list,
        "dog_personality_list": dog_personality_list,
        "cat_size_list": cat_size_list,
        "cat_personality_list": cat_personality_list,
    }
    return render(request, "dogwalking/index.html", context)


def create(request):
    if request.method == "POST":
        # tags = request.POST.get("tags", "").split(",")
        dogwalking_form = DogwalkingForm(request.POST, request.FILES)
        pet = Pet.objects.get(pk=request.POST.get('pet_need_caring'))
        if dogwalking_form.is_valid():
            dogwalking = dogwalking_form.save(commit=False)
            dogwalking.pet = pet
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


def detail(request, dogwalking_pk):
    dogwalking = Dogwalking.objects.get(pk=dogwalking_pk)
    reviews = Review.objects.filter(id=dogwalking_pk)
    comments = dogwalking.comment_set.all()
    form = CommentForm()
    dogwalking.save()
    context = {
        "dogwalking": dogwalking,
        "comments": comments,
        "form": form,
        "reviews": reviews,
    }
    return render(request, "dogwalking/detail.html", context)


def update(request, dogwalking_pk):
    dogwalking = Dogwalking.objects.get(pk=dogwalking_pk)
    if request.user == dogwalking.user:
        if request.method == "POST":
            dogwalking_form = DogwalkingForm(
                request.POST, request.FILES, instance=dogwalking
            )

            if dogwalking_form.is_valid():
                dogwalking_form.save()
                return redirect("dogwalking:detail", dogwalking_pk)
        else:
            dogwalking_form = DogwalkingForm(instance=dogwalking)

        context = {
            "dogwalking_form": dogwalking_form,
            "dogwalking": dogwalking,
        }

        return render(request, "dogwalking/update.html", context)
    else:
        return redirect(request, "dogwalking/update.html", dogwalking_pk)


def delete(request, dogwalking_pk):
    Dogwalking.objects.get(pk=dogwalking_pk).delete()
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


def comment_create(request, dogwalking_pk):
    dogwalking_data = Dogwalking.objects.get(pk=dogwalking_pk)

    if request.user.is_authenticated:
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.dogwalking = dogwalking_data
            comment.user = request.user
            comment.save()
    return redirect("dogwalking:detail", dogwalking_pk)


def comment_delete(request, dogwalking_pk, comment_pk):
    comment_data = Comment.objects.get(pk=comment_pk)

    if request.user == comment_data.user:
        comment_data.delete()
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


# 리뷰
@login_required
def review(request, pk):
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.dogwalking_id = pk
            review.save()
            return redirect("dogwalking:detail", pk)
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "dogwalking/review.html", context)


def review_update(request, dogwalking_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.dogwalking_id = dogwalking_pk
            review.save()
            return redirect("bars:detail", dogwalking_pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
    }
    return render(request, "dogwalking/review_update.html", context)


def review_delete(request, dogwalking_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
        return redirect("dogwalking:detail", dogwalking_pk)
    # else:
    #     return HttpResponseForbidden
