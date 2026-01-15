from django.urls import path

from apps.pages import views


app_name = "pages"

urlpatterns = [
    path("about-me/", views.about, name="about_me")
]
