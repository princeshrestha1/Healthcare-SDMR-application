from account.models import User
from django.db import models
from auditlog.registry import auditlog


class Appointment(models.Model):
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='doctor')
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    is_emergency = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient.full_name} --> {self.doctor.full_name}"

auditlog.register(Appointment)
