from datetime import datetime
import pytz

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader, Context, Template

from .models import Task

# https://docs.djangoproject.com/en/2.2/topics/auth/default/
@login_required
def all(request):
    all_tasks = Task.objects.all()

    return render(request, 'tasks/all.html', {'all_tasks': all_tasks})


def index(request):
    now = datetime.today()
    todays_tasks = Task.objects.filter(due=now)

    context = {
        'date': now.date,
        'todays_tasks': todays_tasks,
    }

    return render(request, 'tasks/index.html', context)


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/detail.html', {'task': task})
