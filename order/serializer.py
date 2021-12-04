from re import I
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"