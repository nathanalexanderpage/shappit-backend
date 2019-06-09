from django.urls import path
from . import views

urlpatterns = [
    # all info necessary for new shipment record
    path('new_shipment_info', views.new_shipment_info, name='new_shipment_info'),
    # all barges
    path('barges', views.barge, name='barges_index'),
    # all voyages associated with certain barge
    path('barges/<int:barge_id>/voyages', views.voyages_using_barge, name='voyages_using_barge'),
    # all customers
    path('customers', views.customers_index, name='customers_index'),
    # all contact files for given customer
    path('customers/<int:customer_id>/contacts', views.addresses_for_customer, name='addresses_for_customer'),
    # all customer standings
    path('customerstandings', views.customer_standings, name='customer_standings'),
    # all shipments associated with a shipper
    path('customer/<int:customer_id>/<str:role>/shipments', views.shipments_with_customer_as, name='shipments_with_customer_as'),
    # all service centers
    path('service_centers', views.service_centers, name='service_centers'),
    # all shipments to/from service center
    path('service_centers/<str:service_center>/<str:origin_or_destination>/shipments', views.shipments_to_or_from_service_center, name='shipments_to_or_from_service_center'),
    # all equipment
    path('equipment', views.equipment, name='equipment'),
    # all shipments that were housed in specified equipment
    path('equipment/<int:equipment_id>/shipments', views.shipments_using_equipment, name='shipments_using_equipment'),
    # all equipment types
    path('eqt_types', views.equipment_types, name='equipment_types'),
    # all equipment of certain type
    path('eqt_types/<int:eqt_type>/equipment', views.equipment_of_type, name='equipment_of_type'),
    # all payment methods
    path('payment_methods', views.payment_methods, name='payment_methods'),
    # single shipment post
    path('shipment', views.shipment_init, name='shipment_init'),
    # single shipment get/put/delete
    path('shipment/<int:pk>', views.shipment_postop, name='shipment_postop'),
    # all tugs
    path('tugs', views.tugs, name='tugs'),
    # all voyages for which tug was used
    path('tugs/<int:tug_id>/voyages', views.voyages_using_tug, name='voyages_using_tug'),
    # all voyages
    path('voyages', views.voyages, name='voyages'),
    # path('dogs/<int:pk>/', views.dog_detail, name='dog_detail'),
    # path('dog_toys/<int:pk>/', views.dog_detail, name='dog_detail')
]
