from django.contrib import admin
from django.urls import path 
from .views import DoctorListView, DetailDoctorView, DepartmentDetailView, DoctorAvailabilityView
from rest_framework.routers import  DefaultRouter
from .viewsets import DetailDoctorViewSets

router = DefaultRouter()
router.register('doctors', DetailDoctorViewSets)

urlpatterns = [
    path('doctor/', DoctorListView.as_view()),
    path('doctor/<pk>', DetailDoctorView.as_view() ),
    path('doctor/<pk>/availability', DoctorAvailabilityView.as_view()),
    path('doctor/<pk>/department', DepartmentDetailView.as_view())
] + router.urls