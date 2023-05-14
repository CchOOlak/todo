from rest_framework import generics, permissions

from core.models import User
from core.serializers import RegisterSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer