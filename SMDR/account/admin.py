from django.contrib import admin
from .models import User, Relatives
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
# from vendor.models import GrowerProfile
# from utills.permissions import IsVendor
from django.db.models import Q


# class CustomUserAdmin(UserAdmin):
#     # model = User
#     list_display = ['email', 'avatar', 'first_name', 'last_name', 'phone_no',
#                     'is_active', 'is_admin', ]
#     # list_filter = ['email', 'is_active', 'is_creator', 'is_editor','is_staff']
#     readonly_fields = ['is_admin', ]
#     # fieldsets = (

#     #     (None, {'fields': ('first_name', 'avatar',
#     #      'last_name', 'email', 'phone_no')}),

#     #     ('Permissions', {'fields': ('is_admin', 'is_active', )}),
#     # )

#     search_fields = ('email',)
#     ordering = ('email',)


# admin.site.register(User, CustomUserAdmin)
admin.site.register(User)


class RelativesAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(__class__, self).get_form(request, obj, **kwargs)
        form.base_fields['relative'].queryset = User.objects.filter(is_doctor=False)
        form.base_fields['patient'].queryset = User.objects.filter(is_doctor=False)
        return form

admin.site.register(Relatives, RelativesAdmin)