from django.shortcuts import render, redirect

from core.models import Task
from core.serializers import UserRegisterSerializer, TaskSerializer
from core.views import task as task_views


def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(author=request.user)
    else:
        tasks = []
    tasks = task_views.TaskViewSet.as_view({'get':'list'})(request).data
    
    context = {
        "status_enum": Task.status_enum,
        "priority_enum": Task.priority_enum,

        "date_descending": "-created_at",
        "date_ascending": "created_at",
        "priority_descending": "-priority",
        "priority_ascending": "priority",

        "tasks": tasks,
    }
    return render(request, 'index.html', context=context)

def register_view(request):
    serializer = UserRegisterSerializer()
    return render(request, 'register.html', context={'form': serializer})

def task_view(request, pk=None):
    try:
        if pk is None:
            task = TaskSerializer()
            empty_task = True
        else:
            task = TaskSerializer(Task.objects.get(pk=pk))
            empty_task = False
        return render(request, 'task.html', context={
            'task': task,
            'empty_task': empty_task,
            })
    except Exception as e:
        print(e)
        return redirect('index')
