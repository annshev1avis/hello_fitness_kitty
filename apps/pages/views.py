from django.http import HttpResponse


def about(request):
    return HttpResponse("Страница обо мне")
