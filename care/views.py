from django.shortcuts import render, redirect, get_object_or_404
from .models import Care, Comment, Review
from accounts.models import Pet
from .forms import Careform, CommentForm, ReviewForm
from django.db.models import Q
import re
from django.contrib.auth.decorators import login_required

# from django.views.generic import ListView, TemplateView
from django.http import JsonResponse

# Create your views here.


def index(request):
    care = Care.objects.order_by("-pk")
    pet = Pet.objects.all()
    pet_species = request.GET.getlist("species")  # 강아지 고양이
    # animal = request.GET.getlist('caring_animal') # 돌봄가능 동물
    time = request.GET.getlist("caring_time")  # 돌봄가능 시간
    etc = request.GET.getlist("etc")  # 기타
    areas = request.GET.get("area")  # 지역
    gender = request.GET.get("gender")  # 돌보미 성별
    print(gender)
    # print(pet_species)

    # 매칭 조건

    # 돌봄가능 동물별
    species_list = ["강아지", "고양이"]
    # 돌봄가능 기간별
    caring_time_list = ["4시간이하", "1일이하", "3일이하", "7일이하", "7일초과"]
    # 기타
    etc_list = ["사전만남가능", "반려동물있음", "노견/노모케어가능", "픽업가능", "산책가능", "돌봄경력있음"]
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
    # 성별
    gender_list = ["남자", "여자"]

    # DB모델
    if pet_species:
        query = Q()
        for i in pet_species:
            query = query | Q(species__icontains=i)
            pet = pet.filter(query)
            # print(query)
    if time:
        query = Q()
        for i in time:
            query = query | Q(caring_time__icontains=i)
            care = care.filter(query)
    if etc:
        query = Q()
        for i in etc:
            query = Q(etc__icontains=i)
            care = care.filter(query)
    if areas:
        query = Q()
        for i in areas:
            query = Q(area__icontains=i)
            care = care.filter(query)
    if gender:
        query = Q()
        for i in gender:
            query = query | Q(gender__icontains=i)
            care = care.filter(query)
        

    context = {
        "care": care,
        "pet": pet,
        "time": time,
        "etc": etc,
        "areas": areas,
        "gender": gender,
        "species_list": species_list,
        "caring_time_list": caring_time_list,
        "etc_list": etc_list,
        "area_list": area_list,
        "gender_list": gender_list,
    }
    return render(request, "care/index.html", context)


def more(request):
    pet = Pet.objects.all()
    pet_species = request.GET.getlist("species")  # 강아지 고양이
    time = request.GET.getlist("caring_time")  # 돌봄가능 시간
    etc = request.GET.getlist("etc")  # 기타
    areas = request.GET.get("area")  # 지역
    gender = request.GET.get("gender")  # 돌보미 성별
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

    if more_what == 'find-petsitter':
        care = Care.objects.filter(writing_down=0).order_by('-pk')
    elif more_what == 'found-petsitter':
        care = Care.objects.filter(writing_down=1).order_by('-pk')
    
    # DB모델
    if pet_species:
        query = Q()
        for i in pet_species:
            query = query | Q(species__icontains=i)
            pet = pet.filter(query)
            # print(query)
    if time:
        query = Q()
        for i in time:
            query = query | Q(caring_time__icontains=i)
            care = care.filter(query)
    if etc:
        query = Q()
        for i in etc:
            query = Q(etc__icontains=i)
            care = care.filter(query)
    if areas:
        query = Q()
        for i in areas:
            query = Q(area__icontains=i)
            care = care.filter(query)
    if gender:
        query = Q()
        for i in gender:
            query = query | Q(gender__icontains=i)
            care = care.filter(query)

    context = {
        'care': care,
        'area_list': area_list,
        'more_what': more_what,
    }
    
    return render(request, "care/more.html", context)


def create(request):
    if request.method == "POST":
        # tags = request.POST.get("tags", "").split(",")
        care_form = Careform(request.POST, request.FILES)
        pet = Pet.objects.get(pk=request.POST.get("pet_need_caring"))
        if care_form.is_valid():
            care = care_form.save(commit=False)
            care.pet = pet
            care.caring_animal = pet.species
            care.gender = request.POST.get("gender")
            care.caring_time = request.POST.get("caring_time")
            care.etc = request.POST.getlist("etc")
            care.user = request.user
            care.save()
            # for tag in tags:
            #     tag = tag.strip()
            #     if tag != "":
            #         dogwalking.tags.add(tag)
            return redirect("care:detail", care.pk)
    else:
        care_form = Careform()
    context = {
        "care_form": care_form,
    }
    return render(request, "care/create.html", context)


def detail(request, care_pk):
    care = Care.objects.get(pk=care_pk)
    reviews = Review.objects.filter(care=care)
    review = reviews[0] if reviews else ''
    comments = care.comment_set.all()
    form = CommentForm()
    care.save()

    p = re.compile("[가-힣//]+")
    etcs = p.findall(care.etc)

    context = {
        "care": care,
        "comments": comments,
        "form": form,
        "etcs": etcs,
        "review": review,
    }
    return render(request, "care/detail.html", context)


def update(request, care_pk):
    care = Care.objects.get(pk=care_pk)
    if request.user == care.user:
        if request.method == "POST":
            care_form = Careform(request.POST, request.FILES, instance=care)
            pet = Pet.objects.get(pk=request.POST.get("pet_need_caring"))
            if care_form.is_valid():
                care = care_form.save(commit=False)
                print("넘어가나?22")
                care.pet = pet
                care.caring_animal = pet.species
                care.gender = request.POST.get("gender")
                care.caring_time = request.POST.get("caring_time")
                care.etc = request.POST.getlist("etc")
                care.user = request.user
                care.save()
                return redirect("care:detail", care_pk)
        else:
            care_form = Careform(instance=care)

        context = {
            "care": care,
            "care_form": care_form,
        }

        return render(request, "care/update.html", context)
    else:
        return redirect(request, "care/update.html", care_pk)


def delete(request, care_pk):
    Care.objects.get(pk=care_pk).delete()
    return redirect("care:index")


def writing(request, care_pk):
    care = Care.objects.get(pk=care_pk)
    if request.user == care.user:
        if care.writing_down:
            care.writing_down = False
        else:
            care.writing_down = True
        care.save()
    return redirect('care:index')


def caring(request, care_pk):
    care = Care.objects.get(pk=care_pk)
    
    if care.user != request.user:
        care.caring = request.user
        care.writing_down = True
        care.save()

    return redirect("care:index")


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


# 리뷰
@login_required
def review(request, pk):
    care = Care.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.care = care
            review.grade = request.POST.get('reviewStar')
            review.save()
            return redirect("care:detail", pk)
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
        'care': care,
    }
    return render(request, "care/review.html", context)


def review_update(request, care_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.care_id = care_pk
            review.save()
            return redirect("bars:detail", care_pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
    }
    return render(request, "care/review_update.html", context)


def review_delete(request, care_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
        return redirect("care:detail", care_pk)
    # else:
    #     return HttpResponseForbidden
