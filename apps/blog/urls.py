from django.urls import path

from apps.blog import views


app_name = "blog"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("posts/", views.posts, name="all_posts"),
    path("posts/random/", views.random_post, name="random_post"),
    path("posts/<slug:post_slug>/", views.single_post, name="single_post"),
    path("categories/<slug:category_slug>/", views.category, name="category"),
]