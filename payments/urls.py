from django.urls import path
from . import views

urlpatterns = [
    path('initiate-payment/', views.initiate_payment),
    path('check-payment-status/', views.check_payment_status),
    path('refund-payment/', views.refund_payment),
]