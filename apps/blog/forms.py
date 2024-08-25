from django import forms
from django.forms import ModelForm
from .models import Article, Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name':'Nombre de la Categoría'
        }


class ArticleForm(ModelForm):
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None, label='Categoría')
    class Meta:
        model = Article
        fields = ['title', 'pub_date', 'content', 'category_id']
        labels = {
            'title':'Título', 
            'pub_date':'Fecha de Publicación', 
            'content':'Contenido', 
            'category_id':'Categoría'
        }
        error_messages = {
            'title':{
                'max_length':'Este campo es requerido',
            }
        }

