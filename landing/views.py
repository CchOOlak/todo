from django.shortcuts import render

from core.models import Task
from core.serializers import UserRegisterSerializer


def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(author=request.user)
    else:
        tasks = []
    return render(request, 'index.html', context={"tasks": tasks})

def register(request):
    serializer = UserRegisterSerializer()
    return render(request, 'register.html', context={'form': serializer})
