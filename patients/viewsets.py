from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import PatientSerializer, MedicalRecordSerializer
from .models import Patient, MedicalRecord
from rest_framework.decorators import action

class DetailPatientViewSets (viewsets.ModelViewSet):
    allowed_methods = ['GET', 'PUT', 'DELETE', 'POST']
    serializer_class = MedicalRecordSerializer
    queryset = Patient.objects.all()

@action(["POST"], detail=True, url_path='add_medical_record')
def add_medical_record(self, request, pk):
    patient = self.get_object()
    data = request.data
    data['patient'] = patient.id
    serializer = MedicalRecordSerializer(data=data)
    
    if serializer.is_valid():
        try:
            serializer.save()
            return Response({"status": "Medical Record added successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@action(['GET'], detail=True, url_path='medical-record')
def list_medical_history(self, request, pk=None):
    patient = self.get_object()  
    medical_history = MedicalRecord.objects.filter(patient=patient)  
    serializer = MedicalRecordSerializer(medical_history, many=True)
    return Response(serializer.data)

