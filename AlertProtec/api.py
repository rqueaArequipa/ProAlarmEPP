from .models import Machinery, Person, User
from rest_framework import viewsets, permissions, filters
from .serializer import MachinerySerializer, PersonSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend

class MachineryViewSet(viewsets.ModelViewSet):
    queryset = Machinery.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MachinerySerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'