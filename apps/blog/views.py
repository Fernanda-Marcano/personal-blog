from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Article
from .forms import CategoryForm, ArticleForm

# =================== Creating views of Category ==============
def create_category(request):
    if request.method == 'POST':
        form_category = CategoryForm(request.POST or None)
        if form_category.is_valid():
            form_category.save()
            return HttpResponse('Funciona Correctamente')
        else:
            return HttpResponse('Ha ocurrido un error')
    form_category = CategoryForm()
    context = {
        'category':form_category,
    }
    return render(request, 'category/create.html', context)


def list_category(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'category/list.html', context)


def edit_category(request, id):
    category_id = Category.objects.get(id=id)
    if request.method == 'POST':
        form_category = CategoryForm(request.POST or None, instance=category_id)
        if form_category.is_valid():
            form_category.save()
            return HttpResponse(f'La categoria {category_id} fue editada correctamente')
        else:
            return HttpResponse('No se pudo editar la categoria')
    form_category = CategoryForm(instance=category_id)
    context = {
        'category':form_category,
    }
    return render(request, 'category/edit.html', context)


def delete_category(request, id):
    category_id = Category.objects.get(id=id)
    category_id.delete()
    return redirect(to='list-category')


# ================ Creating views of Article ===============

def create_article(request):
    if request.method == 'POST':
        form_article = ArticleForm(request.POST or None)
        if form_article.is_valid():
            form_article.save()
            return HttpResponse('Articulo agregado correctamente')
        else:
            return HttpResponse('Ha ocurrido un error al crear el articulo')
    form_article = ArticleForm()
    context = {'form_article':form_article}
    return render(request, 'article/create.html', context)


def list_article(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'article/list.html', context)


def list_category_article(request, id):
    category_id = Category.objects.get(id=id)
    articles = category_id.article.all()
    context = {
        'category_id':category_id,
        'articles':articles,
    }
    return render(request, 'article/category_article.html', context)


def edit_article(request, id):
    article_id = Article.objects.get(id=id)
    if request.method == 'POST': 
        form_article = ArticleForm(request.POST or None, instance=article_id)
        if form_article.is_valid():
            form_article.save()
            return redirect(to='list-category')
        else:
            return HttpResponse('No se pudo editar el articulo')
    form_article = ArticleForm(instance=article_id)
    context = {
        'form_article':form_article
    }
    return render(request, 'article/edit.html', context)


def detail_article(request, id):
    article_id = Article.objects.get(id=id)
    context = {'article':article_id}
    return render(request, 'article/detail.html', context)


def delete_article(request, id):
    article_id = Article.objects.get(id=id)
    article_id.delete()
    return redirect(to='list-category')
