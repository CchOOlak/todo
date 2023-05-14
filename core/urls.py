from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from rest_framework import routers

from core.views import TaskViewSet, UserRegisterView

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # path('search/<slug:str>/', search),
]
