from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import *


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            # somente Admin tem permissão de escrita
            return request.user.is_staff


class AddressPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            try:
                # se o request.user for um Client, vai retornar False
                is_client = Client.objects.get(email=request.user.email)
                if is_client:
                    return False
            except Client.DoesNotExist:
                # se não for um Client, vai retornar True
                return True


class ClientPermissions(BasePermission):
    def has_permission(self, request, view):
        try:
            is_client = Client.objects.get(email=request.user.email)
            if is_client:
                return False
        except Client.DoesNotExist:
            return True


class ManagerPermissions(BasePermission):
    def has_permission(self, request, view):
        try:
            is_client = Client.objects.get(email=request.user.email)
            if is_client:
                return False
        except Client.DoesNotExist:
            return True


class EmployeePermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            # somente Manager e Admin possuem permissão de escrita
            try:
                is_manager = Manager.objects.get(email=request.user.email)
                if is_manager:
                    return True
            except Manager.DoesNotExist:
                return request.user.is_staff


class DemandListPermissions(BasePermission):
    def has_permission(self, request, view):
        try:
            is_client = Client.objects.get(email=request.user.email)
            if is_client:
                return False
        except Client.DoesNotExist:
            return True


class DemandDetailPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            try:
                is_client = Client.objects.get(email=request.user.email)
                if is_client:
                    return obj.client.user == request.user
            except Client.DoesNotExist:
                return True
        else:
            try:
                is_client = Client.objects.get(email=request.user.email)
                if is_client:
                    return False
            except Client.DoesNotExist:
                return True


# class IsClientOwn(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return obj.user == request.user
#         else:
#             try:
#                 clientEmail = Client.objects.get(email=request.user.email).email
#                 return request.user.email != clientEmail
#             except Client.DoesNotExist:
#                 return True


# class ClientAndEmployeeUnallowed(BasePermission):
#     def has_permission(self, request, view):
        
#         try:
#             managerEmail = Manager.objects.get(email=request.user.email).email
#             if managerEmail:
#                 return True
#         except Manager.DoesNotExist:
#             if request.user.is_staff:
#                 return True
#             else:
#                 return False


# class IsEmployeeOwn(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return obj.user == request.user
#         else:
#             try:
#                 employeeEmail = Employee.objects.get(email=request.user.email).email
#                 return request.user.email != employeeEmail
#             except Employee.DoesNotExist:
#                 return True


# class PizzaPermissions(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         else:
#             # somente Manager e Admin podem criar Pizzas
#             try:
#                 is_manager = Manager.objects.get(email=request.user.email)
#                 if is_manager:
#                     return True
#             except Manager.DoesNotExist:
#                 return request.user.is_staff
