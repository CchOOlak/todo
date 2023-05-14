from rest_framework.permissions import BasePermission

class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('POST', 'GET', 'HEAD', 'OPTIONS'):
            return True
        return request.user == obj.author
