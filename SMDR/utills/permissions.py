from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, SAFE_METHODS
from account.models import Relatives

class IsAdminUserOrReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


class IsDoctor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_doctor or False


class IsPatient(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user_obj = request.user.is_doctor
        if user_obj:
            return False
        return True


class IsRelatives(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return Relatives.objects.get(id=request.user.id)