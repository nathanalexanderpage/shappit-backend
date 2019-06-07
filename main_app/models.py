from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Barge(models.Model):
    name = models.CharField(max_length=60)

class CustomerStanding(models.Model):
    code = models.IntegerField()
    desc = models.CharField(max_length=50)

class Customer(models.Model):
    name = models.CharField(max_length=60)
    credit_limit = models.IntegerField(blank=True, default=2000)
    standing = models.ForeignKey(CustomerStanding, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CustomerContact(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True, default='')
    address_city = models.CharField(max_length=50)
    address_state = models.CharField(max_length=50)
    address_zip = models.IntegerField()


class EquipmentType(models.Model):
    name = models.CharField(max_length=20, default='dry')

class Equipment(models.Model):
    no = models.CharField(primary_key=True, max_length=10)
    status = models.CharField(max_length=10, default='empty')
    type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)

class PaymentMethod(models.Model):
    name = models.CharField(max_length=60)

class ServiceCenter(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=3)
    lat = models.CharField(max_length=11)
    lng = models.CharField(max_length=11)

class Shipment(models.Model):
    no = models.IntegerField()
    origin = models.ForeignKey(ServiceCenter, on_delete=models.CASCADE, related_name='shipments_originating')
    destination = models.ForeignKey(ServiceCenter, on_delete=models.CASCADE, related_name='shipments_delivering')
    shipper = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='shipments_shipped_by')
    consignee = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='shipments_consigned_to')
    billto = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='shipments_billed_to')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

class PaymentTransaction(models.Model):
    made_by = models.CharField(max_length=60)
    input_by = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    date_time = models.IntegerField()
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=True, blank=True) # CHANGE ONCE FULLY SET UP TO DISALLOW UNLINKED PAYMENTS
    card_last_four = models.IntegerField(null=True, blank=True)
    note = models.CharField(max_length=255, blank=True, default='')

class Tug(models.Model):
    name = models.CharField(max_length=40)
    status = models.CharField(max_length=20)
    last_lng = models.CharField(max_length=11)
    last_lat = models.CharField(max_length=11)

class Voyage(models.Model):
    no = models.CharField(max_length=60)
    tug = models.ForeignKey(Tug, on_delete=models.CASCADE)
    barge = models.ForeignKey(Barge, on_delete=models.CASCADE)
    current_sequence = models.IntegerField(default=0)
    finished = models.BooleanField(default=False)

class Stop(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    sequence = models.IntegerField()
    service_center = models.ForeignKey(ServiceCenter, on_delete=models.CASCADE)
    arrival_expected = models.IntegerField()
    arrival_actual = models.IntegerField(null=True, blank=True)
    departure_expected = models.IntegerField()
    departure_actual = models.IntegerField(null=True, blank=True)
