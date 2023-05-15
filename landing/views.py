from django.shortcuts import render, redirect

from core.models import Task
from core.serializers import UserRegisterSerializer, TaskSerializer


def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(author=request.user)
    else:
        tasks = []
    return render(request, 'index.html', context={"tasks": tasks})

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
