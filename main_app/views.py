from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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

# @api_view(['GET', 'POST'])
# def dogs_index(request):
#     if request.method == 'GET':
#         dogs = Dog.objects.all()
#         serializer = DogSerializer(dogs, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = DogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# BARGES
@api_view(['GET'])
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

# all shipments that used specified container
@api_view(['GET'])
def shipments_using_container(request, equipment_id):
    if request.method == 'GET':
        shipments_queryset = Shipment.objects.filter(equipment=equipment_id)
        json_ready = list(shipments_queryset)
        shipments_data = serializers.serialize('json', json_ready)
        print(shipments_data)
        return Response(shipments_data)
    else:
        return Response('error: not GET method')

@api_view(['GET'])
def addresses_for_customer(request, customer_id):
    if request.method == 'GET':
        addresses_queryset = CustomerContact.objects.filter(customer_id=customer_id)
        json_ready = list(addresses_queryset)
        addresses_data = serializers.serialize('json', json_ready)
        print(addresses_data)
        return Response(addresses_data)
    else:
        return Response('error: not a GET method')

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


@api_view(['GET'])
def customer_standings_list(request):
    if request.method == 'GET':
        customer_standings = CustomerStanding.objects.all()
        serializer = CustomerStandingSerializer(customer_standings, many=True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET'])
def customer_standing(request):
    if request.method == 'GET':
        customer_standing = test_resp
        return Response(customer_standing)
    else:
        return Response('error: not GET method')

@api_view(['GET'])
def customers_index(request):
    if request.method == 'GET':
        result_customers = Customer.objects.all()
        serializer = CustomerSerializer(result_customers, many=True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)



#
# @api_view(['GET', 'POST'])
# def dog_toys_index(request):
#     if request.method == 'GET':
#         dog_toys = Dog.objects.all()
#         serializer = DogToySerializer(dog_toys, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = DogToySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
