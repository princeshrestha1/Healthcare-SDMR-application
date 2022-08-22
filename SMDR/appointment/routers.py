from rest_framework.routers import DefaultRouter
from appointment.views import *

router = DefaultRouter()

router.register('doctor', DoctorAppointmentViewSets, basename='doctor-appointment')
router.register('patient', PatientAppointmentViewSets, basename='patient-appointment')
router.register('relative', RelativeAppointmentViewSets, basename='relative-appointment')