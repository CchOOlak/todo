from django.shortcuts import redirect, render

from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Task
from core.serializers import TaskSerializer
from core.filters import TaskOrderingFilter
from core.permissions import IsOwnerPermission


class TaskViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerPermission,]
    filter_backends = (DjangoFilterBackend, TaskOrderingFilter,)
    filterset_fields = ('priority', 'status',)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(author=self.request.user)
        else:
            return Task.objects.filter(pk=0)

    def create(self, request, *args, **kwargs):
        super(TaskViewSet, self).create(request, *args, **kwargs)
        return redirect('index')
    
    def update(self, request, *args, **kwargs):
        super(TaskViewSet, self).update(request, *args, **kwargs)
        return redirect('index')

    def destroy(self, request, *args, **kwargs):
        super(TaskViewSet, self).destroy(request, *args, **kwargs)
        return redirect('index')
