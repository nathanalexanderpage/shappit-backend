from rest_framework import serializers
from .models import Barge, Customer, CustomerContact, CustomerStanding, Equipment, EquipmentTypeDetails, PaymentMethod, PaymentTransaction, ServiceCenter, Shipment, Stop, Tug, Voyage

# class DogToySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DogToy
#         fields = ('id', 'name', 'color')
#
# class DogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Dog
#         fields = ('id', 'name', 'desc', 'age', 'user', 'dog_toys')

class BargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barge
        fields = ('id', 'name')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'credit_limit', 'standing')

class CustomerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerContact
        fields = ('id', 'customer', 'phone', 'address_line_1', 'address_line_2', 'address_city', 'address_zip')

class CustomerStandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerStanding
        fields = ('id', 'code', 'desc')

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'no', 'status', 'type')

class EquipmentTypeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentTypeDetails
        fields = ('id', 'name')

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ('id', 'name')

class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = ('id', 'made_by', 'input_by', 'date_time', 'method', 'note')
