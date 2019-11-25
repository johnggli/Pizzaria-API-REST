from django.shortcuts import render
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView

from .models import *
from .serializers import *

from .permissions import *
from rest_framework import permissions

from rest_framework import filters
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter


class ApiRoot(GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            "user": reverse(UserList.name, request=request),
            "address": reverse(AddressList.name, request=request),
            "client": reverse(ClientList.name, request=request),
            "manager": reverse(ManagerList.name, request=request),
            "employee": reverse(EmployeeList.name, request=request),
            "progress": reverse(ProgressList.name, request=request),
            "pizza": reverse(PizzaList.name, request=request),
            "demand": reverse(DemandList.name, request=request),
        }, status=status.HTTP_200_OK)


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = "user-list"

    permission_classes = (permissions.IsAdminUser,)
    

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = "user-detail"

    permission_classes = (permissions.IsAdminUser,)


class AddressList(ListCreateAPIView):
    name = 'address-list'
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    permission_classes = (permissions.IsAuthenticated, AddressPermissions,)


class AddressDetail(RetrieveUpdateDestroyAPIView):
    name = 'address-detail'
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    permission_classes = (permissions.IsAuthenticated, AddressPermissions,)


class ClientList(ListCreateAPIView):
    name = 'client-list'
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    permission_classes = (permissions.IsAuthenticated, ClientPermissions,)


class ClientDetail(RetrieveUpdateDestroyAPIView):
    name = 'client-detail'
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    permission_classes = (permissions.IsAuthenticated, ClientPermissions,)


class ManagerList(ListCreateAPIView):
    name = 'manager-list'
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly, ManagerPermissions,)


class ManagerDetail(RetrieveUpdateDestroyAPIView):
    name = 'manager-detail'
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly, ManagerPermissions,)


class EmployeeList(ListCreateAPIView):
    name = 'employee-list'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    filter_fields = ('salary',) # filtra por salário
    search_fields = ('^name',) # busca funcionários cujo nome começa com a palavra pesquisada
    ordering_fields = ('name', 'salary',) # ordena por nome ou salário, crescente ou decrescente

    permission_classes = (permissions.IsAuthenticated, EmployeePermissions,)


class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    name = 'employee-detail'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    permission_classes = (permissions.IsAuthenticated, EmployeePermissions,)


class ProgressList(ListCreateAPIView):
    name = 'progress-list'
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly,)


class ProgressDetail(RetrieveUpdateDestroyAPIView):
    name = 'progress-detail'
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly,)


class PizzaList(ListCreateAPIView):
    name = 'pizza-list'
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    filter_fields = ('price',) # filtra por preço
    search_fields = ('^name',) # busca pizzas que começam com a palavra pesquisada
    ordering_fields = ('name', 'price',)

    permission_classes = (IsAdminOrReadOnly,)


class PizzaDetail(RetrieveUpdateDestroyAPIView):
    name = 'pizza-detail'
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    permission_classes = (IsAdminOrReadOnly,)


class DemandList(ListCreateAPIView):
    name = 'demand-list'
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer

    permission_classes = (permissions.IsAuthenticated, DemandListPermissions,)


class DemandDetail(RetrieveUpdateDestroyAPIView):
    name = 'demand-detail'
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer

    permission_classes = (permissions.IsAuthenticated, DemandDetailPermissions,)
