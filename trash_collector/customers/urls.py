from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('registercustomer/', views.create, name='registercustomer'),
    path('setpickup/', views.setpickup,
         name="setpickup"),
    path('pickup_suspension/', views.pickup_suspension,
         name="pickup_suspension"),
    path('account_info/', views.account_info,
         name="account_info"),
    path('onetime_pickup/', views.onetime_pickup, name="onetime_pickup")
]
