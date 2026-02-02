from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path


urlpatterns = [
    path("", include("apps.blog.urls")),
    path("", include("apps.pages.urls")),
    path("users/", include("apps.users.urls")),
    re_path(r"mdeditor/", include("mdeditor.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += debug_toolbar_urls()
