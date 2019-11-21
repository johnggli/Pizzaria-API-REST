from django.shortcuts import render
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView

from .models import *
from .serializers import *


class ApiRoot(GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            "address": reverse(AddressList.name, request=request),
            "client": reverse(ClientList.name, request=request),
            "manager": reverse(ManagerList.name, request=request),
            "employee": reverse(EmployeeList.name, request=request),
            "progress": reverse(ProgressList.name, request=request),
            "pizza": reverse(PizzaList.name, request=request),
            "demand": reverse(DemandList.name, request=request),
        }, status=status.HTTP_200_OK)


class AddressList(ListCreateAPIView):
    name = 'address-list'
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetail(RetrieveUpdateDestroyAPIView):
    name = 'address-detail'
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class ClientList(ListCreateAPIView):
    name = 'client-list'
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(RetrieveUpdateDestroyAPIView):
    name = 'client-detail'
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ManagerList(ListCreateAPIView):
    name = 'manager-list'
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerDetail(RetrieveUpdateDestroyAPIView):
    name = 'manager-detail'
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class EmployeeList(ListCreateAPIView):
    name = 'employee-list'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    name = 'employee-detail'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ProgressList(ListCreateAPIView):
    name = 'progress-list'
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer


class ProgressDetail(RetrieveUpdateDestroyAPIView):
    name = 'progress-detail'
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer


class PizzaList(ListCreateAPIView):
    name = 'pizza-list'
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaDetail(RetrieveUpdateDestroyAPIView):
    name = 'pizza-detail'
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class DemandList(ListCreateAPIView):
    name = 'demand-list'
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer


class DemandDetail(RetrieveUpdateDestroyAPIView):
    name = 'demand-detail'
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer
