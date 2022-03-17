from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from . import serializers, models

# Create your views here.
@api_view(["GET"])
def Company(request):
    companies = models.Company.objects.all()
    serializer = serializers.CompanySerializer(companies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def Material(request):
    materials = models.Material.objects.all()
    serializer = serializers.MaterialSerializer(materials, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
