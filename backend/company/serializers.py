from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from . import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = "__all__"


class CompanyMaterialPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyMaterialPricing
        fields = "__all__"
