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
import re

# Create your views here.
def index(request):
    dogwalking = Dogwalking.objects.order_by("-pk")
    pet = Pet.objects.all()
    pet_species = request.GET.getlist('pet_species') # 견종
    pet_characteristics = request.GET.getlist('characteristics') # 반려동물 성격
    area = request.GET.get('area') # 지역

    # 매칭

    # 견종
    pet_species_list = ['강아지', '고양이']
    # 반려동물 성격
    pet_characteristics_list = ['활발한', '소심한', '긍정적인', '적응력높은', '충성심높은', '애교많은', '예민한', '호기심많은', '겁이많은']
     # 지역별
    area_list = [
        "경기도",
        "서울시",
        "부산광역시",
        "경상남도",
        "인천광역시",
        "경상북도",
        "대구광역시",
        "충청남도",
        "전라남도",
        "전라북도",
        "충청북도",
        "강원도",
        "대전광역시",
        "광주광역시",
        "울산광역시",
        "제주도",
        "세종시",
    ]
    # 글 내림


    # DB모델
    if pet_species:
        query = Q()
        for i in pet_species:
            query = query | Q(species__icontains=i)
            pet = pet.filter(query)
    if pet_characteristics:
        query = Q()
        for i in pet_characteristics:
            query = query | Q(characteristics__icontains=i)
            pet = pet.filter(query)
    if area:
        query = Q()
        for i in area:
            query = Q(area__icontains=i)
            dogwalking = dogwalking.filter(query)


    context = {
        "dogwalking": dogwalking,
        "pet": pet,
        "pet_species": pet_species,
        "pet_characteristics": pet_characteristics,
        "area": area,
        "pet_species_list": pet_species_list,
        "pet_characteristics_list": pet_characteristics_list,
        "area_list":area_list,
    }
    return render(request, "dogwalking/index.html", context)


def more(request):
    pet = Pet.objects.all()
    pet_species = request.GET.getlist('pet_species') # 견종
    pet_characteristics = request.GET.getlist('characteristics') # 반려동물 성격
    area = request.GET.get('area') # 지역
    more_what = request.GET.get('more')
    
    # 지역별
    area_list = [
        "경기도",
        "서울시",
        "부산광역시",
        "경상남도",
        "인천광역시",
        "경상북도",
        "대구광역시",
        "충청남도",
        "전라남도",
        "전라북도",
        "충청북도",
        "강원도",
        "대전광역시",
        "광주광역시",
        "울산광역시",
        "제주도",
        "세종시",
    ]

    if more_what == 'find-friends':
        dogwalking = Dogwalking.objects.filter(writing_down=0).order_by('-pk')
    elif more_what == 'found-friends':
        dogwalking = Dogwalking.objects.filter(writing_down=1).order_by('-pk')
    
    # DB모델
    if pet_species:
        query = Q()
        for i in pet_species:
            query = query | Q(species__icontains=i)
            pet = pet.filter(query)
    if pet_characteristics:
        query = Q()
        for i in pet_characteristics:
            query = query | Q(characteristics__icontains=i)
            pet = pet.filter(query)
    if area:
        query = Q()
        for i in area:
            query = query | Q(area__icontains=i)
            dogwalking = dogwalking.filter(query)

    context = {
        'dogwalking': dogwalking,
        'area_list': area_list,
        'more_what': more_what,
    }
    
    return render(request, "dogwalking/more.html", context)


def create(request):
    if request.method == "POST":
        # tags = request.POST.get("tags", "").split(",")
        dogwalking_form = DogwalkingForm(request.POST, request.FILES)
        pet = Pet.objects.get(pk=request.POST.get('pet'))
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
    reviews = Review.objects.filter(dogwalking=dogwalking)
    review = reviews[0] if reviews else ''
    comments = dogwalking.comment_set.all()
    form = CommentForm()
    dogwalking.save()

    p = re.compile("[가-힣//]+")
    characteristics = p.findall(dogwalking.pet.characteristics)

    context = {
        "dogwalking": dogwalking,
        "comments": comments,
        "form": form,
        "review": review,
         "characteristics": characteristics,
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


def writing(request, dogwalking_pk):
    dogwalking = Dogwalking.objects.get(pk=dogwalking_pk)
    if request.user == dogwalking.user:
        if dogwalking.writing_down:
            dogwalking.writing_down = False
        else:
            dogwalking.writing_down = True
        dogwalking.save()
    return redirect('dogwalking:detail', dogwalking_pk)

def walking(request, dogwalking_pk):
    dogwalking = Dogwalking.objects.get(pk=dogwalking_pk)
    
    if dogwalking.user != request.user:
        if dogwalking.walking.filter(pk=request.user.pk).exists():
            dogwalking.walking.remove(request.user)
        else:
            dogwalking.walking.add(request.user)
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
    dogwalking = Dogwalking.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.dogwalking = dogwalking
            review.grade = request.POST.get('reviewStar')
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
