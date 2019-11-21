from rest_framework.serializers import ModelSerializer
from .models import *


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ProgressSerializer(ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'


class PizzaSerializer(ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'


class DemandSerializer(ModelSerializer):
    class Meta:
        model = Demand
        fields = '__all__'