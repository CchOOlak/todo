from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Task
from core.serializers import TaskSerializer
from core.filters import TaskOrderingFilter
from core.permissions import IsOwnerPermission


class TaskViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerPermission,]
    filter_backends = (DjangoFilterBackend, TaskOrderingFilter,)
    filter_fields = ('priority', 'status',)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
