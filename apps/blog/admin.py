from django import forms
from django.contrib import admin

from apps.blog import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    
    fieldsets = [
        (None, {"fields": ["name", "description"]}),
        ("Служебные настройки", {"fields": ["slug"]})
    ]


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "name", "description", "category", "is_published", "pub_datetime"
    ]
    fieldsets = [
        (None, {"fields": ["name", "description", "category", "content", "slug"]}),
        ("Настройки видимости", {"fields": ["is_published"]}),
        ("Неизменяемые поля", {"fields": ["pub_datetime", "edited_datetime", "views", "minutes_to_read"]})
    ]
    readonly_fields = ["pub_datetime", "edited_datetime", "views", "minutes_to_read"]
    search_fields = ["name", "description", "content"]
    
    def get_form(self, request, obj = ..., change = ..., **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields["description"].widget = forms.Textarea()
        return form

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)
