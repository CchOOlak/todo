from django.urls import path

from landing.views import index, register_view, task_view


urlpatterns = [
    path('', index, name='index'),
    path('register/', register_view, name='register-view'),
    path('task/<int:pk>/', task_view, name='task-view'),
]