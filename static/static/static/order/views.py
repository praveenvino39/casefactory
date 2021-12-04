import json
from django.db.models import manager
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.fields import JSONField
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import order

from order.serializer import OrderSerializer
from .models import Order
# Create your views here.


@api_view(["POST"])
def create_order(request):
    order = Order(model =request.POST.get("model"),
    model_id=request.POST.get("model_id"),
    design_image=request.FILES.get("design_image"),
    price =request.POST.get("price"))
    order.save()
    response = OrderSerializer(order, many = False)
    return Response(order.data)


@api_view(["GET"])
def get_orderby_id(request, id):
    order = get_object_or_404(Order, id=id)
    print(order)
    response = OrderSerializer(data=order, many = False)
    return Response(response.data)


@api_view(["GET"])
def get_all_order(request):
    data = Order.objects.all()
    response = OrderSerializer(data, many=True)
    return Response(response.data)