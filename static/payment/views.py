from django.shortcuts import render

# Create your views here.


def order_info(request):
    return render(request, 'payment/payment.html')