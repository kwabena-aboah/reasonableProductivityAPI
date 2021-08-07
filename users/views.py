# from django.shortcuts import render
from rest_framework import viewsets
from . serializer import UserSerializer, UserProfileSerializer
from . models import User, UserProfile


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
