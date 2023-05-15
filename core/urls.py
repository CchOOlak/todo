from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from rest_framework import routers

from core.views import TaskViewSet, UserRegisterView


urlpatterns = [
    # path('', include(router.urls)), 

    path('tasks/', TaskViewSet.as_view({
        'get': 'list',
        'post': 'create',
        }), name='tasks-list'),
    path('tasks/<int:pk>/', TaskViewSet.as_view({
        'get': 'retrieve',
        'post': 'update',
    }), name='tasks-detail'),
    path('tasks/<int:pk>/delete', TaskViewSet.as_view({
        'get': 'retrieve',
        'post': 'destroy',
    }), name='tasks-delete'),

    path('auth/register/', UserRegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),

    # path('search/<slug:str>/', search),
]
