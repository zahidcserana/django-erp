from django.db.models import Q

from commontag.templatetags.myapptags import status_task
from tag.models import Tag
from project.models import Project
from .models import Task
from .forms import TaskForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect


def task_index(request):
    search = request.GET.get('search')
    project = request.GET.get('project')
    status = request.GET.get('status')
    tag = request.GET.get('tag')
    if search is not None:
        q = Q()
        if not project == '':
            q &= Q(project=project)
        if not status == '':
            q &= Q(status=status)
        if not tag == '':
            q &= Q(tag=tag)

        tasks = Task.objects.filter(q)
    else:
        tasks = Task.objects.all().select_related('user')

    page = request.GET.get('page', 1)

    paginator = Paginator(tasks, 5)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context = {
        "data": data,
        "status": status_task,
        'tag': Tag.objects.all(),
        'project': Project.objects.all()
    }
    return render(request, 'task_index.html', context)


def task_add(request):
    if request.method == 'POST':
        task_form = TaskForm(data=request.POST)
        if task_form.is_valid():
            task = task_form.save()
            current_user = request.user
            task.user_id = current_user.id
            task.save()
            return redirect('task_index')
    else:
        task_form = TaskForm()
    context = {
        "form": task_form,
    }
    return render(request, "task_add.html", context)


def task_detail(request, pk=None):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('task_detail', pk)
        else:
            print(task_form.errors)
    else:
        task_form = TaskForm(instance=task)
    context = {
        "add": False,
        "task": task,
        "form": task_form
    }
    return render(request, "task_detail.html", context)
