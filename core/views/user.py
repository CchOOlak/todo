from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import TemplateView

from rest_framework import permissions

from core.models import User
from core.serializers import UserRegisterSerializer


class UserRegisterView(TemplateView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer
    template_name = 'register.html'

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=False):
            try:
                serializer.create(serializer.validated_data)
                user = User.objects.get(username=serializer.validated_data['username'])
                login(request, user)
                return redirect('index')
            except:
                return render(request, 'register.html', {'error': 'duplicate error'})
        return render(request, 'register.html', {'form': serializer})

    def get(self, request):
        serializer = UserRegisterSerializer()
        return render(request, 'register.html', {'form': serializer})
