from django import forms
from django.forms import ModelForm
from .models import Article, Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']
        labels = {
            'name':'Nombre de la Categoría', 
            'image':'Imagen',
        }
        error_messages = {
            'name':{
                'max_length':'Este campo es requerido',
            }
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control-file'})
        }


class ArticleForm(ModelForm):
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None, label='Categoría', widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Article
        fields = ['title', 'content', 'category_id']
        labels = {
            'title':'Título', 
            'content':'Contenido', 
            'category_id':'Categoría'
        }
        error_messages = {
            'title':{
                'max_length':'Este campo es requerido',
            }
        }
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }

