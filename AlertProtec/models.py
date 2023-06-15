from django.db import models

class Machinery(models.Model):
    type_machinery = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    num_serial = models.IntegerField(default=0)
    year = models.IntegerField(default=2010)
    capacity = models.IntegerField(default=0)
    type_fuel = models.CharField(max_length=50)
    hour = models.IntegerField(default=0)
    date_maintenance = models.DateField('date maintenance')
    status = models.CharField(max_length=100)
    type_engine = models.CharField(max_length=100)
    img = models.CharField(max_length=250, blank=True)
    
    def __str__(self):
        return self.type_machinery

class Person(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.CharField(max_length=8)
    number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    date_birth = models.DateField()
    address = models.CharField(max_length=50)
    certifications = models.CharField(max_length=200)
    rol = models.IntegerField(default=0)
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200)
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    rol = models.IntegerField(default=0)
    date_created = models.DateField(auto_now_add=True)
    avatar = models.CharField(max_length=250, blank=True)
    def __str__(self):
        return self.username

class Alert(models.Model):
    status = models.IntegerField(default=0) #1 Activado y 0 desactivado
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.status
    



