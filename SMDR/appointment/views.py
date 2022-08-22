from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from utills.permissions import IsPatient, IsDoctor, IsRelatives
from .serializers import *


class PatientAppointmentViewSets(ModelViewSet):
    permission_classes = [IsPatient, permissions.IsAuthenticated]
    serializer_class = PatientAppointmentSerializer
    queryset = Appointment.objects.all()

    def get_queryset(self):
        return self.queryset.filter(patient=self.request.user)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save(patient=request.user)
            return Response(user.data)
        return Response(serializer.errors, status=400)
    

    def update(self, request, pk=None):
        obj = self.get_object()
        serializer = self.serializer_class(instance=obj)
        if serializer.is_valid():
            user = serializer.save(patient=request.user)
            return Response(user.data)
        return Response(serializer.errors, status=400)


class DoctorAppointmentViewSets(ModelViewSet):
    permission_classes = [IsPatient, permissions.IsAuthenticated]
    serializer_class = PatientAppointmentSerializer
    queryset = Appointment.objects.all()

    def get_queryset(self):
        return self.queryset.filter(doctor=self.request.user)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save(doctor=request.user)
            return Response(user.data)
        return Response(serializer.errors, status=400)
    

    def update(self, request, pk=None):
        obj = self.get_object()
        serializer = self.serializer_class(instance=obj)
        if serializer.is_valid():
            user = serializer.save(doctor=request.user)
            return Response(user.data)
        return Response(serializer.errors, status=400)


class RelativeAppointmentViewSets(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = RelativesAppointmentSerializer
    permission_classes = [IsRelatives,permissions.IsAuthenticated]
    http_method_names = ['post']