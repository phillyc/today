from django.contrib import admin

from .models import Tag, Comment, Task


models = [Comment]
admin.site.register(models)
admin.site.site_header = 'Dev Today admin'
admin.site.site_title = 'Dev Today admin'

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    search_fields = ['title']
    list_display = ('title', 'created', 'due', 'completed',)
    list_filter = ('tags',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['text']
    list_display = ('text', )
    list_filter = ('text', )
