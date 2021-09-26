from articles.models import Article
from django.contrib import admin

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display= ('pk', 'title')

admin.site.register(Article, ArticleAdmin)