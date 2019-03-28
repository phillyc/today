from django.db import models
from django.utils import timezone


class Category(models.Model):
    # money, pilot, study, chores, etc.
    category = models.CharField(max_length=255, blank=False)

    class Meta:
        verbose_name_plural = "categories"


class Comment(models.Model):
    # When the task is deleted, delete any comments.
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField('date created', default=timezone.now)
    modified = models.DateTimeField('date updated', default=timezone.now)
    completed = models.DateTimeField('date completed', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True) # home, garage, office, garden, etc.
    categories = models.ManyToManyField(Category, blank=True)
    estimated = models.IntegerField(blank=True, null=True)  # 5, 30, and 60 minute increments
    actual = models.IntegerField(blank=True, null=True)
    due = models.DateTimeField('due date', blank=True, null=True)
    archived = models.BooleanField(default=False) # Hidden, press delete twice to really delete.
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True) # task could be a sub-task
    # recurring - optional(something to dictate this should happen every Monday)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Task, self).save(*args, **kwargs)


