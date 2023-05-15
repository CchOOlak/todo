from rest_framework.filters import OrderingFilter


class TaskOrderingFilter(OrderingFilter):
    allowed_custom_filters = ['created_at', '-created_at', '-priority', 'priority',]

    def get_ordering(self, request, queryset, view):
        param = request.query_params.get(self.ordering_param)
        if param and param in self.allowed_custom_filters:
            return param
        return '-created_at'

    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        return queryset.order_by(ordering)
