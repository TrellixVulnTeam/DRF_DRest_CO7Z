from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission): #предоставление доступа для редактирования записей в БД только создателям данной записи
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

