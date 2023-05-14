from django.shortcuts import render

from core.models import Task
from core.serializers import UserRegisterSerializer


def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(author=request.user)
    else:
        tasks = []
    return render(request, 'index.html', context={"tasks": tasks})

def register_view(request):
    serializer = UserRegisterSerializer()
    return render(request, 'register.html', context={'form': serializer})

def task_view(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        return render(request, 'task.html', context={'task': task})
    except:
        return index(request)
