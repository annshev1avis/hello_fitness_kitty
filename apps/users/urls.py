from django.urls import path

from apps.users import views

app_name = "users"

urlpatterns = [
    path("favorites/<int:post_id>/check/", views.is_in_favorites, name="check-favorites"),
    path("favorites/<int:post_id>/", views.toggle_favorite, name="toggle-favorite"),
]