from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.urls import reverse

from apps.blog.models import Post
from apps.users.forms import UserCreateForm, UserUpdateForm


def registration(request):
    if request.user.is_authenticated:
        return redirect("users:profile")
        
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("users:profile"))
    else:
        form = UserCreateForm()

    return render(request, "users/registration.html", {"form": form})


def profile(request):
    if not request.user.is_authenticated:
        return render(
            request,
            "users/unlogined_profile.html",
        )
    
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(
        request,
        "users/profile.html",
        {
            "user": request.user,
            "form": form,
        }
    )
