from django.contrib import admin

from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'is_breaking', 'published', 'source')
    list_filter = ('language', 'is_breaking', 'source')
    search_fields = ('title', 'summary')
