from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from . import serializers, models

# Create your views here.
@api_view(["POST"])
def register(request):
    serializer = serializers.RegisterUserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def login(request):
    serializer = serializers.LoginUserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST", "PUT", "DELETE"])
def account(request):
    user = get_object_or_404(User, key=request.data["id"]).user
    account = get_object_or_404(models.Account, user=user)
    # get profile data
    if request.method == "POST":
        serializer = serializers.AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # update profile data
    elif request.method == "PUT":
        if request.data.get("name") != None and request.data.get("name") != "":
            account.name = request.data.get("name")

        account.save()
        serializer = serializers.AccountSerializer(account)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # delete profile and user
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_200_OK)
