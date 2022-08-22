from .models import Appointment
from rest_framework import serializers


class PatientAppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.IntegerField(read_only=True)
    class Meta:
        model = Appointment
        fields = "__all__"


class DoctorAppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.IntegerField(read_only=True)
    class Meta:
        model = Appointment
        fields = "__all__"


class RelativesAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"