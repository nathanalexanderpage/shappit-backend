from django.urls import path
from . import views

urlpatterns = [
    # all barges
    path('barges/', views.barge, name='barges_index'),
    # all voyages associated with certain barge
    path('barges/<int:barge_id>/voyages/', views.voyages_using_barge, name='voyages_using_barge'),
    # all shipments associated with a shipper
    path('customer/<int:customer_id>/<str:role>/shipments', views.shipments_with_customer_as, name='shipments_with_customer_as'),
    # all shipments to/from service center
    path('<str:service_center>/<str:origin_or_destination>/shipments', views.shipments_to_or_from_service_center, name='shipments_to_or_from_service_center'),

    # all shipments that used specified container
    # path('container/<int:equipment_id>/shipments/', views.shipments_using_equipment, name='shipments_using_equipment'),
    
    # all shipments associated with a consignee
    # path('customer/<int:pk>/consignee/shipments'),
    # all shipments associated with a bill-to
    # path('customer/<int:pk>/billto/shipments'),
    # path('dogs/<int:pk>/', views.dog_detail, name='dog_detail'),
    # path('dog_toys/<int:pk>/', views.dog_detail, name='dog_detail')
]
