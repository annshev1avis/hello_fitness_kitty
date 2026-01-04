import math
import re

from django.contrib import admin
from django.db import models
from mdeditor.fields import MDTextField


FIND_H2_PATTERN = re.compile(r"^## (.+)", re.MULTILINE)


class Category(models.Model):
    # Основные поля
    name = models.CharField("Название", max_length=200)
    description = models.CharField(
        "Описание для страницы категории",
        max_length=500
    )
    slug = models.SlugField("Cлаг", unique=True)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        
    def __str__(self):
        return self.name
    

class Post(models.Model):
    # Основные поля
    name = models.CharField("Название", max_length=200)
    description = models.TextField(
        "Краткое описание",
        help_text="Одно-два предложения",
        max_length=200,
    )
    content = MDTextField(
        "Содержание поста",
        help_text="""Используйте формат .md. 
        Доступные теги: 'p', 'h2',
        'h3', 'h4', 'ul', 'ol', 'li',
        'strong', 'em', 'a', 'code', 'pre', 
        'blockquote'"""
    )
    cover = models.FileField(
        "Обложка",
        upload_to="post_covers/",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.RESTRICT,
        verbose_name="Категория",
        related_name="posts",
    )
    slug = models.SlugField("Слаг", unique=True)
    recommended_posts = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        verbose_name="Рекомендуемые посты",
        help_text='Посты, которые рекомендуются после прочтения этого'
    )
    
    # Настройки видимости
    is_published = models.BooleanField("Опубликован", default=False)
    
    # Неизменяемые поля
    pub_datetime = models.DateTimeField("Время публикации", auto_now_add=True)
    edited_datetime = models.DateTimeField("Последнее редактирование", auto_now=True)
    views = models.IntegerField("Количество просмотров", default=0)
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-pub_datetime']

    def __str__(self):
        return f"'{self.name}'"
    
    @property
    @admin.display(description="Время чтения (мин.)")
    def minutes_to_read(self):
        """
        Время чтения статьи в минутах
        """
        word_count = len(self.content.split())
        avg_reading_speed = 200  # слов в минуту
        
        return math.ceil(word_count / avg_reading_speed)
    
    @property
    def table_of_contents(self):
        """
        Формирует содержание статьи, извлекая список заголовков 2-го уровня
        """
        return FIND_H2_PATTERN.findall(self.content)
