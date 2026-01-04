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
        "name",
        "description",
        "category",
        "is_published",
        "pub_datetime"
    ]
    
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "name",
                    "description",
                    "category",
                    "content",
                    "slug",
                    "cover",
                    "recommended_posts"
                ]
            }
        ),
        (
            "Настройки видимости",
            {
                "fields": ["is_published"]
            }
        ),
        (
            "Неизменяемые поля",
            {
                "fields": [
                    "pub_datetime",
                    "edited_datetime",
                    "views",
                    "minutes_to_read",
                    "table_of_contents_formatted"
                ]
            }
        )
    ]
    
    readonly_fields = [
        "pub_datetime",
        "edited_datetime",
        "views",
        "minutes_to_read",
        "table_of_contents_formatted"
    ]
    
    search_fields = [
        "name",
        "description",
        "content"
    ]
    
    filter_horizontal = ["recommended_posts"]
    
    @admin.display(description="Содержание")
    def table_of_contents_formatted(self, obj):
        """Форматирует оглавление для отображения в админке."""
        result = []
        for title in obj.table_of_contents:
            result.append(f"- {title}")
        return "".join(result)


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)
