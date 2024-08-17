from rest_framework import permissions


class IsStaffPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active and request.user.is_staff
