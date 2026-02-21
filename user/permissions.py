from rest_framework import permissions
from django.contrib.auth.models import User

class is_owner(permissions.BasePermission):
    def has_permission(self, request, view):
        # obj=super().has_permission(request, view)
        try:
            user=User.objects.get(username=request.query_params["username"])

        except:
            return False
        else:
            if request.user.is_superuser:
                return True
            elif not request.user==user:
                return False
            else:
                return True