from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Department, Doctor, DoctorAvailability
from .serializers import DepartmentSerializer, DoctorAvailabilitySerializer, DoctorSerializer
# Create your views here.


class DoctorListView(APIView):
    http_method_names = ['get', 'post']

    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    """
    Detalles de los doctores por primera key
    """
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DepartmentDetailView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class DoctorAvailabilityView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET','PUT','DELETE']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()