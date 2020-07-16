from django.contrib import admin

# Register your models here.
from .models import Customer, SalesPerson

admin.site.register(Customer)
admin.site.register(SalesPerson)
