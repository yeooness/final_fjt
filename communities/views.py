from django.shortcuts import render, redirect, get_object_or_404
from .models import Community, Comment
from .forms import CommunityForm, CommentForm
from django.core.paginator import Paginator
from django.http import JsonResponse
import json

# Create your views here.

def index(request):
    communities = Community.objects.order_by("-pk")

    # 카테고리
    community_name = "모든게시판"
    community_list = ["자유게시판", "후기게시판", "질문게시판", "지식정보"]

    # 각 게시판에서 가장 많은 좋아요 수를 기록한 게시물 1개
    # 게시판 별 상위 4개 좋아요 순

    paginator = Paginator(communities, 9)
    page_number = request.GET.get("board")
    page_obj = paginator.get_page(page_number)

    if request.GET.get("board"):
        name = request.GET.get("board")
        communities = (
            Community.objects.filter(community__contains=name)
            .order_by("-pk")
        )
        if not name:
            community_name = "모든게시판"
        else:
            community_name = name
        # 페이지네이션
        paginator = Paginator(communities, 9)
        page_number = request.GET.get("board")
        page_obj = paginator.get_page(page_number)  # 숫지만

        context = {
            "name": name,
            "communities": communities,
            "community_name": community_name,
            "community_list": community_list,
            "page_obj": page_obj,
        }
        return render(request, "communities/index.html", context)
    else:
        context = {
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
            community_form = CommunityForm(
                request.POST, request.FILES, instance=community
            )

            if community_form.is_valid():
                community_form.save()
                return redirect("communities:detail", community_pk)
        else:
            community_form = CommunityForm(instance=community)

        return render(
            request, "communities/update.html", {"community_form": community_form}
        )
    else:
        return redirect(request, "communities/update.html", community_pk)


def delete(request, community_pk):
    Community.objects.get(pk=community_pk).delete()
    return redirect("communities:index")

# 댓글
def comment_create(request, comment_pk):
    community_data = get_object_or_404(Community, pk=comment_pk)

    if request.user.is_authenticated:
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.community = community_data
            comment.user = request.user
            comment.save()
        return redirect("communities:detail", comment_pk)
    return redirect('accounts:login')

def comment_delete(request, community_pk, comment_pk):
    comment_data = Comment.objects.get(pk=comment_pk)

    if request.user == comment_data.user:
        comment_data.delete()
    return redirect('communities:detail', community_pk)


def like(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    if request.user in community.like_users.all():
        community.like_users.remove(request.user)
        is_liked = False
    else:
        community.like_users.add(request.user)
        is_liked = True
    context = {"is_liked": is_liked, "likeCount": community.like_users.count()}
    return JsonResponse(context)
        