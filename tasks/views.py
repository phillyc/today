from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader, Context, Template

from .models import Task


def index(request):
    now = datetime.today()
    todays_tasks = Task.objects.all()

    # template = loader.get_template('tasks/index.html')
    context = {
        'datetime': now,
        'todays_tasks': todays_tasks,
    }

    return render(request, 'tasks/index.html', context)


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/detail.html', {'task': task})
