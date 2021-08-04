from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Customer


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user

    print(user)
    return render(request, 'customers/index.html')


def setpickup(request):
    user = request.user
    customer = Customer.objects.get(user=user.id)
    if request.method == 'POST':
        customer.pickup_date = request.POST.get('name')
        customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/setpickup.html')


def pickup_suspension(request):
    user = request.user
    customer = Customer.objects.get(user=user.id)
    if request.method == 'POST':
        customer.start_date = request.POST.get('start')
        customer.end_date = request.POST.get('end')
        customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/pickup_suspension.html')


def account_info(request):
    user = request.user
    customer = Customer.objects.get(user=user.id)
    context = {
        'customer': customer
    }
    return render(request, 'customers/accountinfo.html', context)


def onetime_pickup(request):
    user = request.user
    customer = Customer.objects.get(user=user.id)
    if request.method == 'POST':
        customer.onetime_pickup = request.POST.get('pickup')
        customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/onetime_pickup.html')


def create(request):
    user = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        pickup_date = request.POST.get('pickup_date')
        balance = request.POST.get('balance')
        zipcode = request.POST.get('zipcode')
        address = request.POST.get('address')
        new_customer = Customer(name=name, pickup_date=pickup_date,
                                balance=balance, zipcode=zipcode, address=address, user_id=user.id)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/registercustomer.html')
