from django.shortcuts import render
from .models import SalesPerson, Customer
from .form import CustomerForm, SalesPersonForm


# Create your views here.

def salesMaster(request):
    sales_person = SalesPerson.objects.all()
    customer = Customer.objects.all()

    context = {
        'sales_person': sales_person,
        'customer': customer
    }
    return render(request, 'accounts/sales_master.html', context)


def createCustomer(request):
    form = CustomerForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/customer_form.html', context)
