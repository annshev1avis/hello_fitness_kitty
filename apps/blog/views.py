import random

from django.http import HttpResponse, JsonResponse
from django.db.models import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from apps.blog.models import Category, Post


GALLERY_LENGTH = 8
    

def get_posts_by_categories():
    """
    Возвращает посты для главной страницы, сгруппированные по категориям,
    в виде списка словарей:
    [
        {
            "category": Category,
            "posts": QuerySet[Post]
        },
    ]
    """ 
    return [
        {
            "category": category,
            "posts": category.posts.all()[:GALLERY_LENGTH]
        }
        for category
        in Category.objects.prefetch_related("posts")
    ]


def home_page(request):
    return render(
        request,
        "blog/home_page.html",
        {
            "best_5_posts": list(Post.objects.order_by("-views")[:4]),
            "posts_by_category": get_posts_by_categories()
        }
    )


def posts(request):
    posts = Post.objects.all().order_by("-views")
    context = {}
    
    if len(posts) >= 5:
        context["best_5_posts"] = posts[:5]

    context["posts"] = posts
    
    return render(
        request,
        "blog/all_posts.html",
        context,
    )


def single_post(request, post_slug):
    return render(
        request,
        "blog/single_post.html",
        {"post": get_object_or_404(
            Post.objects.select_related("category")
            .prefetch_related("recommended_posts"),
            slug=post_slug
        )}
    )


def random_post(request):
    post = random.choice(Post.objects.all())
    
    return redirect(reverse("blog:single_post", args=[post.slug]))


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category)
    
    return render(
        request,
        "blog/category_page.html",
        {
            "category": category,
            "posts": posts
        }
    )
