from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods

from apps.blog.models import Post


def posts_by_ids(request, posts_ids: str):
    """
    Возвращает информацию о постах в формате JSON
    """
    posts_ids = list(map(int, posts_ids.split(",")))
    
    data = [
        {
            "name": post.name,
            "description": post.description[:60] + "...",
            "slug": post.slug,
            "cover_url": post.cover.url if post.cover else None,
        }
        for post in Post.objects.filter(id__in=posts_ids)
    ]
    
    return JsonResponse(
        data,
        safe=False,
        json_dumps_params={"indent": 4, "ensure_ascii": False}
    )


def is_liked(post_id, user):
    """
    Проверяет, есть ли пост в избранном
    """
    return user.liked_posts.filter(id=post_id).exists()


@login_required()
@require_http_methods(["GET", "POST", "DELETE"])
def favorite(request, post_id):
    """
    Выполняет действия:
    - проверка наличия поста в избранном
    - добавление/удаление из избранного
    для request.user 
    """
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == "GET":
        return JsonResponse({"result": is_liked(post_id, request.user)})
    
    if request.method == "POST":
        request.user.liked_posts.add(post)
        return JsonResponse({"result": "added"})
    
    if request.method == "DELETE":
        request.user.liked_posts.remove(post)
        return JsonResponse({"result": "removed"})

