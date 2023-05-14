from django.urls import path

from landing.views import index, register


urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register_page'),
]