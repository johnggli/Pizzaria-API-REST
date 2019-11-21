from rest_framework.serializers import ModelSerializer
from .models import *


class AddressSerializer(ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'