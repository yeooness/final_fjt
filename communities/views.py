from django.shortcuts import render, redirect, get_object_or_404
from .models import Community, Comment
from .forms import CommunityForm, CommentForm, PostSearchForm
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
import random, re
from django.views.generic import ListView, TemplateView, FormView
from django.db.models import Q, Count

# Create your views here.


def index(request):
    search_form = PostSearchForm()
    name = request.GET.get("board", '자유게시판')
    pet_name = request.GET.get("pet", '전부')

    communities = Community.objects.filter(community=name)
    communities_pet = communities.filter(pet_species=pet_name) if pet_name !='전부' else communities
    articles_ordered_by_pk = communities_pet.order_by("-pk")
    articles_ordered_by_like = communities.annotate(like_users_cnt=Count('like_users')).order_by("-like_users_cnt")[:8]

    # 카테고리
    community_name = "모든게시판"
    community_list = ["자유게시판", "후기게시판", "질문게시판", "지식정보"]
    
    # 페이지네이션
    paginator = Paginator(articles_ordered_by_pk, 10)
    page_number = request.GET.get('page', '1')
    page_obj = paginator.get_page(page_number)

    context = {
            "name": name,
            # "communities_like": communities_like,
            "articles_ordered_by_like": articles_ordered_by_like,
            "community_name": community_name,
            "community_list": community_list,
            "page_obj": page_obj,
            "search_form": search_form,
            'pet_filter': pet_name,
        }

    return render(request, "communities/index.html", context)


def create(request):
    if request.method == "POST":
        tags = request.POST.get("tags", "").split(",")
        community_form = CommunityForm(request.POST, request.FILES)
        if community_form.is_valid():
            community = community_form.save(commit=False)
            community.community = request.POST.get('community')
            community.pet_species = request.POST.get('pet_species')
            community.user = request.user
            community.save()
            for tag in tags:
                tag = tag.strip()
                if tag != "":
                    community.tags.add(tag)
            return redirect("communities:index")
    else:
        community_form = CommunityForm()
    
    context = {
        "community_form": community_form,
        'category': request.GET.get('category', '자유게시판'),
    }

    return render(request, "communities/create.html", context)


def detail(request, community_pk):
    community = Community.objects.get(pk=community_pk)
    comments = community.comment_set.all()
    form = CommentForm()
    community.save()
    context = {
        "community": community,
        "comments": comments,
        "form": form,
    }
    return render(request, "communities/detail.html", context)


def update(request, community_pk):
    community = Community.objects.get(pk=community_pk)

    if request.user == community.user:
        if request.method == "POST":
            tags = request.POST.get("tags", "").split(",")
            community_form = CommunityForm(
                request.POST, request.FILES, instance=community
            )

            if community_form.is_valid():
                community = community_form.save(commit=False)
                community.community = request.POST.get('community')
                community.pet_species = request.POST.get('pet_species')
                community.save()
                for tag in tags:
                    tag = tag.strip()
                    if tag != "":
                        community.tags.add(tag)
                return redirect("communities:detail", community_pk)
        else:
            community_form = CommunityForm(instance=community)
        
        context = {
            "community_form": community_form,
            'community': community,
        }
        return render(request, "communities/update.html", context)
    else:
        return redirect(request, "communities/update.html", community_pk)


def delete(request, community_pk):
    Community.objects.get(pk=community_pk).delete()
    return redirect("communities:index")


# 댓글
def comment_create(request, community_pk):
    community_data = Community.objects.get(pk=community_pk)

    if request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.community = community_data
            comment.user = request.user
            comment.save()
        return redirect("communities:detail", community_pk)
    return redirect("accounts:login")


def comment_delete(request, community_pk, comment_pk):
    comment_data = Comment.objects.get(pk=comment_pk)

    if request.user == comment_data.user:
        comment_data.delete()
    return redirect("communities:detail", community_pk)


# 좋아요
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


# tag
class TagCloudTV(TemplateView):
    template_name = "taggit/taggit_cloud.html"


class TaggedObjectLV(ListView):
    template_name = "taggit/taggit_post_list.html"
    model = Community

    def get_queryset(self):
        return Community.objects.filter(tags__name=self.kwargs.get("tag"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tagname"] = self.kwargs["tag"]
        return context


# search
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = "communities/search.html"

    def form_valid(self, form):
        searchWord = form.cleaned_data["search_word"]
        community_list = Community.objects.filter(
            Q(title__icontains=searchWord) | Q(content__icontains=searchWord)
        ).distinct()

        context = {}
        context["form"] = form
        context["search_term"] = searchWord
        context["object_list"] = community_list

        return render(self.request, self.template_name, context)
