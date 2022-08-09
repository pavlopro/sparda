from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group


class IsSubscriber(BasePermission):
    def has_permission(self, request, view):
        try:
            return Group.objects.get(name="subscribers").user_set.filter(id=request.user.id).exists()
        except Exception:
            return False
