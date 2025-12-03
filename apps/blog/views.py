from django.http import HttpResponse, JsonResponse


def home_page(request):
    return HttpResponse("Home page. Nice to see you")


def posts(request):
    return JsonResponse({"details": "All posts"})


def single_post(request):
    return HttpResponse("Single post")


def category(request):
    return HttpResponse("All posts in category")
