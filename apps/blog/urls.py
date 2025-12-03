from django.urls import path

from apps.blog import views


urlpatterns = [
    path("", views.home_page),
    path("posts/", views.posts),
    path("posts/{post_slug: slug}/", views.single_post),
    path("categories/{category_slug: slug}/", views.category)
]