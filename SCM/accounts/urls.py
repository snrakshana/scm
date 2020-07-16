from django.urls import path
from accounts import views

urlpatterns = [
    path('sales_master/', views.salesMaster, name='sales_master'),
    path('create_customer/', views.createCustomer, name='create_customer'),
]
