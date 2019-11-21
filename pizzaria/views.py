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
            "address": reverse(AddressList.name, request=request)
        }, status=status.HTTP_200_OK)


class AddressList(ListCreateAPIView):
    name = 'address-list'
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetail(RetrieveUpdateDestroyAPIView):
    name = 'address-detail'
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
