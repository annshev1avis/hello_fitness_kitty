from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from apps.blog.models import Post


# Управление лайками
@login_required()
def is_in_favorites(request, post_id):
    return JsonResponse(
        {"result": request.user.liked_posts.filter(id=post_id).exists()}
    )


@login_required()
@require_http_methods(["POST", "DELETE"])
def toggle_favorite(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == "POST":
        request.user.liked_posts.add(post)
        return JsonResponse({"result": "added"})
    
    if request.method == "DELETE":
        request.user.liked_posts.remove(post)
        return JsonResponse({"result": "removed"})
