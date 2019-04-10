from django.db import models
from django.utils import timezone


class Tag(models.Model):
    # money, pilot, study, chores, etc.
    text = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.text


class Comment(models.Model):
    # When the task is deleted, delete any comments.
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created = models.DateTimeField('date created', default=timezone.now)
    modified = models.DateTimeField('date updated', default=timezone.now)
    due = models.DateTimeField('due date', blank=True, null=True)
    completed = models.DateTimeField('date completed', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    estimated = models.IntegerField(blank=True, null=True)  # 5, 30, and 60 minute increments
    actual = models.IntegerField(blank=True, null=True)
    # task could be a sub-task
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True
    )
    archived = models.BooleanField(default=False) # Hidden, press delete twice to really delete.
    # recurring - optional(something to dictate this should happen every Monday)


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Task, self).save(*args, **kwargs)


