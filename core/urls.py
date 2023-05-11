from django.urls import path, include
from rest_framework import routers

from core.views import TaskViewSet, search

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/<slug:str>/', search),
]
