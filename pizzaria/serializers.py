from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import *


class AddressSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ClientSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ManagerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class EmployeeSerializer(HyperlinkedModelSerializer): 
    class Meta:
        model = Employee
        fields = '__all__'


class ProgressSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'


class PizzaSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'


class DemandSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Demand
        fields = '__all__'