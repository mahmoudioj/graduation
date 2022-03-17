from xmlrpc.client import boolean
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    # relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # fields
    is_road_transport = models.BooleanField()
    road_transport_price = models.IntegerField()

    is_sea_freight = models.BooleanField()
    sea_freight_price = models.IntegerField()

    is_customs_clearance = models.BooleanField()

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    rate = models.IntegerField()
    logo = models.ImageField(upload_to="media")

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CompanyMaterialPricing(models.Model):
    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # fields
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    price = models.IntegerField()
