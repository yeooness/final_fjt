from django.shortcuts import render, redirect
from .models import Community
from .forms import CommunityForm
from django.core.paginator import Paginator

# Create your views here.
# 기본 crud 글쓰기를 원버튼으로 통일 글 전체목록이 됨


def index(request):
    communities = Community.objects.order_by("-pk")
    # 글 보기
    block = Community.objects.exclude(user__in=request.user.blocking.all()).order_by("-pk")
    # 글 안보기
    non_block = Community.objects.filter(user__in=request.user.blocking.all()).order_by("-pk")

    # 카테고리
    community_name = "모든게시판"
    community_list = ["자유게시판", "후기게시판", "질문게시판", "지식정보"]

    # at_all = "모두보기"
    paginator = Paginator(block, 9)
    page_number = request.GET.get("board")
    page_obj = paginator.get_page(page_number)

    if request.GET.get("board"):
        name = request.GET.get("board")
        block = (
            Community.objects.filter(community__contains=name)
            .exclude(user__in=request.user.blocking.all())
            .order_by("-pk")
        )
        if not name:
            community_name = "모든게시판"
        else:
            community_name = name
        # 페이지네이션
        paginator = Paginator(block, 9)
        page_number = request.GET.get("board")
        page_obj = paginator.get_page(page_number) # 숫지만

        context = {
            # "at_all": at_all,
            "name": name,
            "communities": communities,
            "community_name": community_name,
            "community_list": community_list,
            "page_obj": page_obj,
        }
        return render(request, "communities/index.html", context)
    else:
        context = {
            # "at_all": at_all,
            "communities": communities,
            "community_name": community_name,
            "community_list": community_list,
            "page_obj": page_obj,
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
    return render(
        request, "communities/create.html", {"community_form": community_form}
    )


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
    else:
        return redirect(request, "communities/update.html", community_pk)

def delete(request, community_pk):
    Community.objects.get(pk=community_pk).delete()
    return redirect("communities:index")
