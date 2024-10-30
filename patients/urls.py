from django.contrib import admin
from django.urls import path 
from patients.views import DetailPatientView, ListPatientsView, InsurancePatientView, MedicalRecordView

urlpatterns = [
    path('patients/', ListPatientsView.as_view()),
    path('patients/<int:pk>', DetailPatientView.as_view()),
    path('patients/<int:pk>/insurance', InsurancePatientView.as_view()),
    path('patients/<int:pk>/medicalrecord', MedicalRecordView.as_view())

]