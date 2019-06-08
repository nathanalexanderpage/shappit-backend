from django.shortcuts import render
from django.http import HttpResponse
from .models import Barge, Customer, CustomerContact, CustomerStanding, Equipment, EquipmentType, PaymentMethod, PaymentTransaction, ServiceCenter, Shipment, Stop, Tug, Voyage
from rest_framework import serializers
from django.core import serializers
from .serializers import BargeSerializer, CustomerSerializer, CustomerContactSerializer, CustomerStandingSerializer, EquipmentSerializer, EquipmentTypeSerializer, PaymentMethodSerializer, PaymentTransactionSerializer, ServiceCenterSerializer, ShipmentSerializer, TugSerializer, StopSerializer, VoyageSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

test_resp = [
    {
        'id': 1,
        'name': 'Test Response'
    }
]

# Create your views here.
# BARGES
@api_view(['GET', 'POST'])
def barge(request):
    if request.method == 'GET':
        barges = Barge.objects.all()
        serializer = BargeSerializer(barges, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BargeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        return Response(serializer.errors)

# CUSTOMERS
@api_view(['GET', 'POST'])
def customers_index(request):
    if request.method == 'GET':
        result_customers = Customer.objects.all()
        serializer = CustomerSerializer(result_customers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        return Response(serializer.errors)

# CUSTOMER CONTACTS
# customer contacts associated with given customer
@api_view(['GET', 'POST'])
def addresses_for_customer(request, customer_id):
    if request.method == 'GET':
        addresses_queryset = CustomerContact.objects.filter(customer_id=customer_id)
        json_ready = list(addresses_queryset)
        addresses_data = serializers.serialize('json', json_ready)
        print(addresses_data)
        return Response(addresses_data)
    elif request.method == 'POST':
        serializer = CustomerContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        return Response('error: not a GET method')

# CUSTOMER STANDINGS
@api_view(['GET', 'POST'])
def customer_standings(request):
    if request.method == 'GET':
        customer_standings = CustomerStanding.objects.all()
        serializer = CustomerStandingSerializer(customer_standings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerStandingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        return Response(serializer.errors)

# EQUIPMENT
@api_view(['GET', 'POST'])
def equipment(request):
    if request.method == 'GET':
        eqt = Equipment.objects.all()
        serializer = EquipmentSerializer(eqt, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        return Response(serializer.errors)

# equipments of type
@api_view(['GET'])
def equipment_of_type(request, customer_id):
    if request.method == 'GET':
        addresses_queryset = CustomerContact.objects.filter(customer_id=customer_id)
        json_ready = list(addresses_queryset)
        addresses_data = serializers.serialize('json', json_ready)
        print(addresses_data)
        return Response(addresses_data)
    else:
        return Response('error: not a GET method')

# EQUIPMENT TYPES
@api_view(['GET', 'POST'])
def equipment_types(request):
    if request.method == 'GET':
        result_equipment_types = EquipmentType.objects.all()
        serializer = EquipmentTypeSerializer(result_equipment_types, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EquipmentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        return Response(serializer.errors)

# PAYMENT METHODS
@api_view(['GET', 'POST'])
def payment_methods(request):
    if request.method == 'GET':
        result_payment_methods = PaymentMethod.objects.all()
        serializer = PaymentMethodSerializer(result_payment_methods, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        return Response(serializer.errors)

# PAYMENT METHODS
@api_view(['GET', 'POST'])
def service_centers(request):
    if request.method == 'GET':
        service_centers = ServiceCenter.objects.all()
        serializer = ServiceCenterSerializer(service_centers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ServiceCenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        return Response(serializer.errors)

# SHIPMENTS
@api_view(['POST'])
def shipment_init(request):
    if request.method == 'POST':
        serializer = ShipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def dog_detail(request, pk):
#     if request.method == 'GET':
#         dog = Dog.objects.get(pk=pk)
#         serializer = DogSerializer(dog)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = DogSerializer(dog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         dog = Dog.objects.get(pk=pk)
#         dog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'DELETE'])
def shipment_postop(request, pk):
    if request.method == 'GET':
        shipment = Barge.objects.get(pk=pk)
        serializer = ShipmentSerializer(barges, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        shipment = Barge.objects.get(pk=pk)
        shipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(serializer.errors)

# all shipments that used specified container
@api_view(['GET'])
def shipments_using_equipment(request, equipment_id):
    if request.method == 'GET':
        shipments_queryset = Shipment.objects.filter(equipment=equipment_id)
        json_ready = list(shipments_queryset)
        shipments_data = serializers.serialize('json', json_ready)
        print(shipments_data)
        return Response(shipments_data)
    else:
        return Response('error: not GET method')

# shipments with given service center either as origin or destination
@api_view(['GET'])
def shipments_to_or_from_service_center(request, service_center, origin_or_destination):
    if request.method == 'GET':
        if origin_or_destination == 'origin':
            shipments_queryset = Shipment.objects.filter(origin=service_center)
        elif origin_or_destination == 'destination':
            shipments_queryset = Shipment.objects.filter(destination=service_center)
        else:
            return Response('error: invalid string entry for "origin or destination"')
    else:
        return Response('error: not GET method')

# shipments with customer as shipper/consignee/bill-to
@api_view(['GET'])
def shipments_with_customer_as(request, customer_id, role):
    if request.method == 'GET':
        if role == 'shipper':
            shipments_queryset = Shipment.objects.filter(shipper=customer_id)
        elif role == 'consignee':
            shipments_queryset = Shipment.objects.filter(consignee=customer_id)
        elif role == 'billto':
            shipments_queryset = Shipment.objects.filter(billto=customer_id)
        else:
            return Response('error: customer role not shipper, consignee, or bill-to')
    else:
        return Response('error: not GET method')

# TUGS
@api_view(['GET', 'POST'])
def tugs(request):
    if request.method == 'GET':
        tugs = Tug.objects.all()
        serializer = TugSerializer(tugs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TugSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        return Response(serializer.errors)

# VOYAGES
# all voyages associated with certain barge
@api_view(['GET'])
def voyages_using_barge(request, barge_id):
    if request.method == 'GET':
        voyages_queryset = Voyage.objects.filter(barge=barge_id)
        json_ready = list(voyages_queryset)
        voyages_data = serializers.serialize('json', json_ready)
        print(voyages_data)
        return Response(voyages_data)
    else:
        return Response('error: not GET method')

# all voyages associated with certain tug
@api_view(['GET'])
def voyages_using_tug(request, tug_id):
    if request.method == 'GET':
        voyages_queryset = Voyage.objects.filter(tug=tug_id)
        json_ready = list(voyages_queryset)
        voyages_data = serializers.serialize('json', json_ready)
        print(voyages_data)
        return Response(voyages_data)
    else:
        return Response('error: not GET method')
