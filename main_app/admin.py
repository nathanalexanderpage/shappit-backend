from django.contrib import admin
from .models import Barge, Customer, CustomerContact, CustomerStanding, Equipment, EquipmentTypeDetails, PaymentMethod, PaymentTransaction, ServiceCenter, Shipment, Stop, Tug, Voyage

# Register your models here.
admin.site.register(Barge)
admin.site.register(Customer)
admin.site.register(CustomerContact)
admin.site.register(CustomerStanding)
admin.site.register(Equipment)
admin.site.register(EquipmentTypeDetails)
admin.site.register(PaymentMethod)
admin.site.register(PaymentTransaction)
admin.site.register(ServiceCenter)
admin.site.register(Shipment)
admin.site.register(Stop)
admin.site.register(Tug)
admin.site.register(Voyage)
