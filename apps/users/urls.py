from django.contrib.auth import views as auth_views
from django.urls import path, include, reverse_lazy

from apps.users import views

app_name = "users"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            next_page=reverse_lazy("users:profile"),
            template_name="users/login.html"
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logged_out.html"),
        name="logout",
    ),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="users/password_change.html",
            success_url=reverse_lazy("users:password_change_done")
        ),
        name="password_change"
    ),
    path(
        "password_change_done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html"
        ),
        name="password_change_done"
    ),
    path("registration/", views.registration, name="registration"),
    path("profile/", views.profile, name="profile"),
]