from django.urls import path

from apps.api import views 


app_name = "api"

urlpatterns = [
    path("posts/<str:posts_ids>/", views.posts_by_ids),
    path(
        "favorites/<int:post_id>/",
        views.favorite,
    ),
]