from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class AddressSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ClientSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('url', 'name', 'email', 'phone', 'address')

    def create(self, validated_data):
        user = User.objects.filter(email=validated_data['email'])
        if user:
            raise serializers.ValidationError("O email '" +
                                              validated_data['email'] +
                                              "' ja está cadastrado")
        else:
            user_created = User.objects.create_user(username=validated_data['name'].split()[0],
                                                email=validated_data['email'],
                                                password='ads2019')
            return Client.objects.create(user=user_created, **validated_data)


class ManagerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ('url', 'name', 'email', 'cpf', 'salary')

    def create(self, validated_data):
        user = User.objects.filter(email=validated_data['email'])
        if user:
            raise serializers.ValidationError("O email '" +
                                              validated_data['email'] +
                                              "' ja está cadastrado")
        else:
            user_created = User.objects.create_user(username=validated_data['name'].split()[0],
                                                email=validated_data['email'],
                                                password='ads2019')
            return Manager.objects.create(user=user_created, **validated_data)


class EmployeeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('url', 'name', 'email', 'cpf', 'salary')

    def create(self, validated_data):
        user = User.objects.filter(email=validated_data['email'])
        if user:
            raise serializers.ValidationError("O email '" +
                                              validated_data['email'] +
                                              "' ja está cadastrado")
        else:
            manager = Manager.objects.get(email=self.context['request'].user.email)
            user_created = User.objects.create_user(username=validated_data['name'].split()[0],
                                                email=validated_data['email'],
                                                password='ads2019')
            return Employee.objects.create(user=user_created, manager=manager, **validated_data)


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


class ManagerEmployeeSerializer(HyperlinkedModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)
    class Meta:
        model = Manager
        fields = ('url', 'name', 'employees',)
