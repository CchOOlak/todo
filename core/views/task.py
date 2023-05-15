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
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerPermission,]
    filter_backends = (DjangoFilterBackend, TaskOrderingFilter,)
    filter_fields = ('priority', 'status',)

    def create(self, request, *args, **kwargs):
        super(TaskViewSet, self).create(request, *args, **kwargs)
        return redirect('index')
    
    def update(self, request, *args, **kwargs):
        super(TaskViewSet, self).update(request, *args, **kwargs)
        return redirect('index')

    def destroy(self, request, *args, **kwargs):
        super(TaskViewSet, self).destroy(request, *args, **kwargs)
        return redirect('index')
