from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Community
from .forms import CommunityForm
# Create your views here.
# 기본 crud 글쓰기를 원버튼으로 통일 글 전체목록이 됨

def index(request):
    communities = Community.objects.order_by("-pk")
    # 카테고리
    community_name = ["자유게시판", "후기게시판", "질문게시판", "지식정보"]
    context = {
        "communities": communities,
        "community_name": community_name,
    }
    return render(request, "communities/index.html", context)

def create(request):
    if request.method == "POST":
        community_form = CommunityForm(request.POST, request.FILES)
        if community_form.is_valid():
            community = community_form.save(commit=False)
            community.user = request.user
            community.save()
            return redirect("communities:index")
    else:
        community_form = CommunityForm()

    return render(request, "communities/create.html", { "community_form": community_form })

def detail(request, community_pk):
    community = Community.objects.get(pk=community_pk)
    context = {
        "community": community,
    }
    return render(request, "communities/detail.html", context)

def update(request, community_pk):
    community = Community.objects.get(pk=community_pk)

    if request.user == community.user:
        if request.method == "POST":
            community_form = CommunityForm(request.POST, request.FILES, instance=community)

            if community_form.is_valid():
                community_form.save()
                return redirect("communities:detail", community_pk)
        else:
            community_form = CommunityForm(instance=community)
        return render(request, "communities/update.html", {"community_form": community_form})

def delete(request, community_pk):
    Community.objects.get(pk=community_pk).delete()
    return redirect("communities:index")