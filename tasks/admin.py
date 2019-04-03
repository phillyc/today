from django.contrib import admin

from .models import Category, Comment, Task


models = [Category, Comment, Task]
admin.site.register(models)
admin.site.site_header = 'Dev Today admin'
admin.site.site_title = 'Dev Today admin'
