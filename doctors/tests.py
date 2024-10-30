from django.test import TestCase
from patients.models import Patient
from doctors.models import Doctor
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
# Create your tests here.

class DoctorViewSetTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
        first_name = 'Joaquin',
        last_name = 'Schmidt',
        date_of_birth = '1997-11-07',
        contact_number = '123123123',
        email = 'ejemplo@example.com',
        adress = 'Direccion de prueba',
        medical_history = 'Ninguno',
        )

        self.doctor = Doctor.objects.create(
            first_name = 'Oscar',
            last_name = 'Lopez',
            qualification = 'Profesional',
            contact_number = '123123123',
            email = 'ejemplo2@example.com',
            adress = 'Argentina',
            biography = 'Sin',
            is_on_vacations = False,
        )
        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse('doctor-appointments', 
                        kwargs={"pk": self.doctor.id},
                        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)