from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Barge(models.Model):
    name = models.CharField(max_length=60)

class Customer(models.Model):
    name = models.CharField(max_length=60)
    credit_limit = models.IntegerField(max_length=11)
    standing = models.ForeignKey(CustomerStanding)

    def __str__(self):
        return self.name

class CustomerContact(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = models.IntegerField(max_length=10)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=50)
    address_city = models.CharField(max_length=50)
    address_state = models.CharField(max_length=50)
    address_zip = models.IntegerField(max_length=9)

class CustomerStanding(models.Model):
    code = models.IntegerField(max_length=3)
    desc = models.CharField(max_length=50)

class Equipment(models.Model):
    no = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    type = models.ForeignKey(EquipmentTypeDetails)

class EquipmentTypeDetails(models.Model):
    name = models.CharField(max_length=20)

class PaymentMethod(models.Model):
    name = models.CharField(max_length=60)

class PaymentTransaction(models.Model):
    made_by = models.CharField(max_length=60)
    method = models.ForeignKey(PaymentMethod)
    note = models.CharField(max_length=255)
    date_time = models.IntegerField(max_length=20)
    origin = models.ForeignKey(ServiceCenter)
    card_last_four = models.IntegerField(max_length=4)

class ServiceCenter(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=3)
    lat = models.AutoField(max_length=11)
    lng = models.AutoField(max_length=11)

class Shipment(models.Model):
    no = models.IntegerField(max_length=60)
    origin = models.ForeignKey(ServiceCenter)
    destination = models.ForeignKey(ServiceCenter)
    shipper = models.ForeignKey(Customer, on_delete=models.CASCADE)
    consignee = models.ForeignKey(Customer, on_delete=models.CASCADE)
    billto = models.ForeignKey(Customer, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment)

class Stop(models.Model):
    voyage = models.ForeignKey(Voyage)
    sequence = models.IntegerField(max_length=2)
    service_center = models.ForeignKey(ServiceCenter)
    arrival_expected = models.IntegerField(max_length=20)
    arrival_actual = models.IntegerField(max_length=20)
    departure_expected = models.IntegerField(max_length=20)
    departure_actual = models.IntegerField(max_length=20)

class Tug(models.Model):
    name = models.CharField(max_length=40)
    status = models.CharField(max_length=20)
    last_lng = models.AutoField(max_length=11)
    last_lat = models.AutoField(max_length=11)

class Voyage(models.Model):
    no = models.CharField(max_length=60)
    tug = models.ForeignKey(Tug)
    barge = models.ForeignKey(Barge)
    current_sequence = models.IntegerField(max_length=2)
    finished = models.BooleanField()
