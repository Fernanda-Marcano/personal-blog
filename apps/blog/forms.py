from django.forms import ModelForm
from .models import Article, Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
