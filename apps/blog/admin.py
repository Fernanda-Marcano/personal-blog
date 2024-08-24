from django.contrib import admin
from .models import Category, Article

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'category_id')
    fields = ['title', 'pub_date', 'content', 'category_id']

admin.site.register(Article, ArticleAdmin)