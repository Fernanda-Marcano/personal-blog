from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Category, Article
from .forms import CategoryForm, ArticleForm

# =================== Creating views of Category ==============
@login_required
def create_category(request):
    if request.method == 'POST':
        form_category = CategoryForm(request.POST, request.FILES)
        if form_category.is_valid():
            form_category.save()
            messages.success(request, 'Categoría creada con éxito')
            return redirect(to='home')
        else:
            messages.error(request, 'Ha ocurrido un error')
            return redirect(to='home')
    form_category = CategoryForm()
    context = {
        'category':form_category,
    }
    return render(request, 'category/create.html', context)


def list_category(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 1)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    context = {
        'categories':categories, 
        'page':page, 
        'post_list':post_list
        }
    return render(request, 'category/list.html', context)

@login_required
def edit_category(request, id):
    category_id = Category.objects.get(id=id)
    if request.method == 'POST':
        form_category = CategoryForm(request.POST, request.FILES, instance=category_id)
        if form_category.is_valid():
            form_category.save()
            messages.success(request, 'Categoría actualizada con éxito')
            return redirect(to='home')
        else:
            messages.error(request, 'Ha ocurrido un error')
            return redirect(to='home')
    form_category = CategoryForm(instance=category_id)
    context = {
        'category':form_category,
    }
    return render(request, 'category/edit.html', context)

@login_required
def delete_category(request, id):
    category_id = Category.objects.get(id=id)
    category_id.delete()
    messages.success(request, 'Categoría eliminada correctamente')
    return redirect(to='home')


# ================ Creating views of Article ===============
@login_required
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
    paginator = Paginator(articles, 1)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    context = {
        'articles':articles, 
        'page':page,
        'post_list':post_list
        }
    return render(request, 'article/list.html', context)
    


def list_category_article(request, id):
    category_id = Category.objects.get(id=id)
    articles = category_id.article.all()
    context = {
        'category_id':category_id,
        'articles':articles,
    }
    return render(request, 'article/category_article.html', context)

@login_required
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

@login_required
def delete_article(request, id):
    article_id = Article.objects.get(id=id)
    article_id.delete()
    messages.success(request, 'Artículo eliminado correctamente')
    return redirect(to='list-article')


def exit(request):
    logout(request)
    return redirect(to='home')