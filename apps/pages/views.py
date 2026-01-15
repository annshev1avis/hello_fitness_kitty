from django.shortcuts import render


def about(request):
    return render(request, "pages/about_me.html", {})
