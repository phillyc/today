from django.contrib import admin

from .models import Category, Comment, Task


models = [Category, Comment, Task]
admin.site.register(models)
