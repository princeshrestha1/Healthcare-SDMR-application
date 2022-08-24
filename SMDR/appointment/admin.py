from django.contrib import admin
from .models import Appointment
from account.models import User




class AppointmentAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(__class__, self).get_form(request, obj, **kwargs)
        form.base_fields['doctor'].queryset = User.objects.filter(is_doctor=True)
        form.base_fields['patient'].queryset = User.objects.filter(is_doctor=False)
        return form

admin.site.register(Appointment, AppointmentAdmin)