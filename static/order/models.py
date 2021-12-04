from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.


class Order(models.Model):
    model = models.CharField(max_length=50,blank=False, null=False)
    model_id = models.PositiveBigIntegerField(null=False, blank=False)
    design_image = models.ImageField()
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    isPaid = models.BooleanField(default=False)
    price = models.PositiveBigIntegerField(null=False)


    def __str__(self) -> str:
        return self.model
