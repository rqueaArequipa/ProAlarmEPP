#from django.shortcuts import render
from .models import Machinery, Person, User, Alert, Device
from rest_framework import viewsets, permissions, filters
from .serializer import MachinerySerializer, PersonSerializer, UserSerializer, AlertSerializer, DiviceSerializer
from django_filters.rest_framework import DjangoFilterBackend

class MachineryViewSet(viewsets.ModelViewSet):
    queryset = Machinery.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MachinerySerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'type_machinery']
    search_fields = ['id', 'type_machinery']
    
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['id', 'name']
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlertSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'status']
    search_fields = ['id', 'status']
    
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DiviceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'