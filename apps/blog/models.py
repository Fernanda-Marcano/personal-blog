from django.db import models
from datetime import date

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='Categoría', max_length=50, blank=False, null=False, unique=True)
    
    def __str__(self):
        return self.name
    
    def clean(self):
        if self.name:
            self.name = self.name.strip().capitalize()
    
    class Meta:
        db_table = 'Category'
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        


class Article(models.Model):
    title = models.CharField(verbose_name='Título', max_length=100, blank=False, null=False, unique=True)
    pub_date = models.DateField(default=date.today)
    content = models.TextField(verbose_name='Contenido', blank=False, null=False)
    category_id = models.ForeignKey('Category', verbose_name='Categoría', on_delete=models.RESTRICT, related_name='article')
    
    def __str__(self):
        return self.title
    
    def clean(self):
        if self.title:
            self.title = self.title.strip().title()
        if self.content:
            self.content = self.content.strip()
    
    class Meta:
        db_table = 'Article'
        ordering = ['pub_date']