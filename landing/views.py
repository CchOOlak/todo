from django.shortcuts import render

from core.serializers import UserRegisterSerializer


def index(request):
    return render(request, 'index.html')

def register(request):
    serializer = UserRegisterSerializer()
    return render(request, 'register.html', context={'form': serializer})
