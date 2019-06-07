from rest_framework import serializers
from .models import Barge, Customer, CustomerContact, CustomerStanding, Equipment, EquipmentType, PaymentMethod, PaymentTransaction, ServiceCenter, Shipment, Stop, Tug, Voyage

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
        fields = ('no', 'status', 'type')

class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = ('id', 'name')

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ('id', 'name')

class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = ('id', 'made_by', 'input_by', 'date_time', 'method', 'note')

class ServiceCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCenter
        fields = ('id', 'name', 'code', 'lat', 'lng')

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ('id', 'no', 'origin', 'destination', 'shipper', 'consignee', 'billto', 'equipment')

class TugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tug
        fields = ('id', 'name', 'status', 'last_lng', 'last_lat')

class VoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyage
        fields = ('id', 'no', 'tug', 'barge', 'current_sequence', 'finished')

class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = ('id', 'voyage', 'sequence', 'service_center', 'arrival_expected', 'arrival_actual', 'departure_expected', 'departure_actual')
