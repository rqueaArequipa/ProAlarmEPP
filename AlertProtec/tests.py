from django.test import TestCase
from .models import Machinery, Person, User, Alert
from django.urls import reverse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from io import BytesIO


class ModelTestCase(TestCase):
    
    #--------------create data structures----------------#
    def setUp(self):
        self.machinery = Machinery.objects.create(
            type_machinery='Excavator',
            model='ABC123',
            num_serial=123456,
            year=2021,
            capacity=100,
            type_fuel='Gas',
            hour=500,
            date_maintenance='2023-01-01',
            status='Active',
            type_engine='Engine A',
            img='machinery.jpg'
        )
        self.person = Person.objects.create(
            name='John',
            last_name='Doe',
            dni='12345678',
            number='1234567890',
            email='john@example.com',
            date_birth='2003-01-01',
            address='123 Main St',
            certifications='Cert A, Cert B',
            machinery=self.machinery
        )
        self.user = User.objects.create(
            username='johndoe',
            password='password',
            person=self.person,
            rol=1,
            avatar='avatar.jpg'
        )
        self.alert = Alert.objects.create(
            status=1,
            person=self.person
        )
    
    #---------------GET, POST, PUT, DELETE --- MACHINERY----------------#
    def test_get_machinery(self):
        url = reverse('machinery-detail', args=[self.machinery.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type_machinery'], self.machinery.type_machinery)
        
    def test_create_machinery(self):
        url = reverse('machinery-list')
        data = {
            'type_machinery': 'Bulldozer',
            'model': 'XYZ789',
            'num_serial': 987654,
            'year': 2022,
            'capacity': 200,
            'type_fuel': 'Diesel',
            'hour': 1000,
            'date_maintenance': '2023-12-31',
            'status': 'Active',
            'type_engine': 'Engine B',
            'img': 'bulldozer.jpg'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Machinery.objects.count(), 2)

    def test_update_machinery(self):
        url = reverse('machinery-detail', args=[self.machinery.id])
        data = {
            'type_machinery': 'Excavator',
            'model': 'ABC123',
            'num_serial': 123456,
            'year': 2021,
            'capacity': 150,
            'type_fuel': 'Diesel',
            'hour': 700,
            'date_maintenance': '2023-01-01',
            'status': 'Inactive',
            'type_engine': 'Engine A',
            'img': 'machinery.jpg'
        }
        response = self.client.put(url, data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Machinery.objects.get(id=self.machinery.id).capacity, 150)

    def test_delete_machinery(self):
        url = reverse('machinery-detail', args=[self.machinery.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Machinery.objects.count(), 0)
        
    #---------------GET, POST, PUT, DELETE --- PERSON----------------#
    def test_get_person(self):
        url = reverse('person-detail', args=[self.person.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.person.name)
        
    def test_create_person(self):
        url = reverse('person-list')
        data = {
            'name': 'Jane',
            'last_name': 'Doe',
            'dni': '87654321',
            'number': '0987654321',
            'email': 'jane@example.com',
            'date_birth': '2005-02-03',
            'address': '456 Second St',
            'certifications': 'Cert C, Cert D'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 2)

    def test_update_person(self):
        url = reverse('person-detail', args=[self.person.id])
        data = {
            'name': 'John',
            'last_name': 'Doe',
            'dni': '12345678',
            'number': '1234567890',
            'email': 'john@example.com',
            'date_birth': '2003-01-01',
            'address': '123 Main St',
            'certifications': 'Cert A, Cert B, Cert C'
        }
        response = self.client.put(url, data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(Person.objects.get(id=self.person.id).certifications.split(', ')), 3)

    def test_delete_person(self):
        url = reverse('person-detail', args=[self.person.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)
        
    #---------------GET, POST, PUT, DELETE --- USER----------------#
    def test_get_user(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
        
    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'username': 'janedoe',
            'password': 'password',
            'person': self.person.id,
            'rol': 1,
            'avatar': 'avatar.jpg'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_update_user(self):
        url = reverse('user-detail', args=[self.user.id])
        data = {
            'username': 'johndoe',
            'password': 'newpassword',
            'person': self.person.id,
            'rol': 2,
            'avatar': 'new_avatar.jpg'
        }
        response = self.client.put(url, data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(id=self.user.id).rol, 2)

    def test_delete_user(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
        
    #---------------GET, POST, PUT, DELETE --- ALERT----------------#
    def test_get_alert(self):
        url = reverse('alert-detail', args=[self.alert.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], self.alert.status)

    def test_create_alert(self):
        url = reverse('alert-list')
        data = {
            'status': 0,
            'person': self.person.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Alert.objects.count(), 2)

    def test_update_alert(self):
        url = reverse('alert-detail', args=[self.alert.id])
        data = {
            'status': 0,
            'person': self.person.id
        }

        # Serializar los datos en formato JSON
        content = JSONRenderer().render(data)
        stream = BytesIO(content)
        parsed_data = JSONParser().parse(stream)
        response = self.client.put(url, parsed_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Alert.objects.get(id=self.alert.id).status, 0)

    def test_delete_alert(self):
        url = reverse('alert-detail', args=[self.alert.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Alert.objects.count(), 0)


'''def test_machinery_str(self):
        machinery = Machinery.objects.get(id=self.machinery.id)
        self.assertEqual(str(machinery), machinery.type_machinery)

    def test_person_str(self):
        person = Person.objects.get(id=self.person.id)
        self.assertEqual(str(person), person.name)

    def test_user_str(self):
        user = User.objects.get(id=self.user.id)
        self.assertEqual(str(user), user.username)

    def test_alert_str(self):
        alert = Alert.objects.get(id=self.alert.id)
        expected_str = str(alert.status)  # Convertir el estado en una cadena
        self.assertEqual(expected_str, str(alert))
    
    def test_machinery_defaults(self):
        machinery = Machinery.objects.create(
            type_machinery='Bulldozer',
            model='XYZ789',
            date_maintenance='2023-11-13'
        )
        self.assertEqual(machinery.num_serial, 0)
        self.assertEqual(machinery.year, 2010)
        self.assertEqual(machinery.capacity, 0)
        self.assertEqual(machinery.type_fuel, '')
        self.assertEqual(machinery.hour, 0)
        self.assertEqual(machinery.status, '')
        self.assertEqual(machinery.type_engine, '')

    def test_person_defaults(self):
        person = Person.objects.create(
            name='Jane',
            last_name='Smith', 
            date_birth = '2003-09-15'
        )
        self.assertEqual(person.dni, '')
        self.assertEqual(person.number, '')
        self.assertEqual(person.email, '')
        self.assertEqual(person.address, '')
        self.assertEqual(person.certifications, '')'''