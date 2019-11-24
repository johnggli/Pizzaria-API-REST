from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import *

class IsAddressOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            # Check permissions for read-only request
            return True
        else:
            # Check permissions for write request
            return obj.pk == request.user.address


class IsAllowedToWrite(BasePermission):
    def has_permission(self, request, view):
        try:
            clientEmail = Client.objects.get(email=request.user.email).email
            return request.user.email != clientEmail
        except Client.DoesNotExist:
            return True
