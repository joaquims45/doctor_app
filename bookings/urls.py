from django.contrib import admin
from django.urls import path 
from .views import MedicalNoteDetailView, AppointmentDetailView, AppointmentListView
urlpatterns = [
    path('appointment/', AppointmentListView.as_view(), name='doctor-appointments'),
    path('appointment/<pk>', AppointmentDetailView.as_view() ),
    path('appiontment/<pk>/medicalnote', MedicalNoteDetailView.as_view()),
]