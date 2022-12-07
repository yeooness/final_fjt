from django.shortcuts import render, redirect, get_object_or_404
from .models import Care, Comment
from .forms import Careform, CommentForm

# from django.views.generic import ListView, TemplateView
from django.http import JsonResponse

# Create your views here.

def index(request):
    care = Care.objects.order_by("-pk")
    animal = request.GET.get('caring_animal') # 돌봄가능 동물
    time = request.GET.get('caring_time') # 돌봄가능 기간
    pet_etc = request.GET.get('etc') # 기타
    areas = request.GET.get('area') # 지역
    gender = request.GET.get('pet_gender') # 펫 성별

    # DB모델
    caring_animal = Care.objects.filter(caring_animal=animal)
    caring_time = Care.objects.filter(caring_time=time)
    etc = Care.objects.filter(etc=pet_etc)
    area = Care.objects.filter(area=areas)
    pet_gender = Care.objects.filter(pet_gender=gender)

    # 매칭 조건
    
    # 돌봄가능 동물별
    caring_animal_list = ["고양이", "강아지"]
    # 돌봄가능 기간별
    caring_time_list = ["4시간이하", "1일이하", "3일이하", "7일이하", "7일초과"]
    # 기타
    etc_list = ["사전만남 가능", "반려동물 있음", "노견/노모 케어 가능", "픽업 가능", "산책 가능", "돌봄 경력 있음"]
    # 지역별
    area_list = ["경기도", "서울시", "부산광역시", "경상남도", "인천광역시", "경상북도", "대구광역시", "충청남도", "전라남도",
     "전라북도", "충청북도", "강원도", "대전광역시", "광주광역시", "울산광역시", "제주도", "세종시"]
    # 성별
    gender_list = ["남자", "여자", "상관없음"]


    context = {
        "care": care,
        "animal": animal,
        "time": time,
        "pet_etc": pet_etc,
        "areas": areas,
        "gender": gender,
        "caring_animal": caring_animal,
        "caring_time": caring_time,
        "etc": etc,
        "area": area,
        "pet_gender": pet_gender,
        "caring_animal_list": caring_animal_list,
        "caring_time_list": caring_time_list,
        "etc_list": etc_list,
        "area_list": area_list,
        "gender_list": gender_list,
    }
    return render(request, "care/index.html", context)


def create(request):
    print(request.POST.get('pet_need_caring'))
    print(request.POST.get('pet_gender'))
    print(request.POST.get('caring_time'))
    print(request.POST.getlist('etc'))





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
    comments = care.comment_set.all()
    form = CommentForm()
    care.save()
    context = {
        "care": care,
        "comments": comments,
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
