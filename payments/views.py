from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from payments.models import PaymentTransaction

@api_view(['POST'])
def initiate_payment(request):
    PaymentTransaction.objects.create(amount=1000)
    return HttpResponse(status=200)

@api_view(['POST'])
def check_payment_status(request):
    last_payment_obj = PaymentTransaction.objects.all().last()
    last_payment_obj.status = "completed"
    last_payment_obj.save()
    return HttpResponse(status=200)

@api_view(['POST'])
def refund_payment(request):
    return Response({'message': 'Payment refunded'})
