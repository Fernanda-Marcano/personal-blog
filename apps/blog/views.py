from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Article
from .forms import CategoryForm, ArticleForm

# =================== Creating views of Category ==============
def create_category(request):
    if request.method == 'POST':
        form_category = CategoryForm(request.POST, request.FILES)
        if form_category.is_valid():
            form_category.save()
            messages.success(request, 'Categoría creada con éxito')
            return redirect(to='list-category')
        else:
            messages.error(request, 'Ha ocurrido un error')
            return redirect(to='list-category')
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
        form_category = CategoryForm(request.POST, request.FILES, instance=category_id)
        if form_category.is_valid():
            form_category.save()
            messages.success(request, 'Categoría actualizada con éxito')
            return redirect(to='list-category')
        else:
            messages.error(request, 'Ha ocurrido un error')
            return redirect(to='list-category')
    form_category = CategoryForm(instance=category_id)
    context = {
        'category':form_category,
    }
    return render(request, 'category/edit.html', context)


def delete_category(request, id):
    category_id = Category.objects.get(id=id)
    category_id.delete()
    messages.success(request, 'Categoría eliminada correctamente')
    return redirect(to='list-category')


# ================ Creating views of Article ===============

def create_article(request):
    if request.method == 'POST':
        form_article = ArticleForm(request.POST or None)
        if form_article.is_valid():
            form_article.save()
            messages.success(request, 'Artículo creado con éxito')
            return redirect(to='list-article')
        else:
            messages.error(request, 'Ha ocurrido un error')
            return redirect(to='list-article')
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
            messages.success(request, 'Artículo actualizado con éxito')
            return redirect(to='list-article')
        else:
            messages.error(request, 'Ha ocurrido un error')
            return redirect(to='list-article')
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
    messages.success(request, 'Artículo eliminado correctamente')
    return redirect(to='list-article')
