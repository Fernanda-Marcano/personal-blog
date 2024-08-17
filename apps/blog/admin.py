from django.contrib import admin
from .models import Category, Article

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    fields = ['title', 'pub_date']

admin.site.register(Article, ArticleAdmin)