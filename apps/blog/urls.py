from django.urls import path
from . import views

urlpatterns = [
    #URLs of Categories
    path('category/create/', views.create_category, name='create-category'),
    path('category/list/', views.list_category, name='list-category'), 
    path('category/edit/<int:id>/', views.edit_category, name='edit-category'), 
    path('category/delete/<int:id>/', views.delete_category, name='delete-category'),
    
    #URLs of Articles
    path('article/create/', views.create_article, name='create-article'), 
    path('article/list/', views.list_article, name='list-article'), 
    path('article/edit/<int:id>/', views.edit_article, name='edit-article'), 
    path('article/delete/<int:id>/', views.delete_article, name='delete-article')
]