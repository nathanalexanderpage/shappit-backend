from django.shortcuts import render
from django.http import HttpResponse
from .models import Barge, Customer, CustomerContact, CustomerStanding, Equipment, EquipmentTypeDetails, PaymentMethod, PaymentTransaction, ServiceCenter, Shipment, Stop, Tug, Voyage
from rest_framework import serializers
from .serializers import BargeSerializer, CustomerSerializer, CustomerContactSerializer, CustomerStandingSerializer, EquipmentSerializer, EquipmentTypeDetailsSerializer, PaymentMethodSerializer, PaymentTransactionSerializer, ServiceCenterSerializer, ShipmentSerializer, TugSerializer, StopSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# # Create your views here.
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
