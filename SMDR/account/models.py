from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .managers import CustomUserManager
# from django.utils.translation import ugettext_lazy
from django.utils import timezone
import uuid
import os


class User(AbstractBaseUser, PermissionsMixin):
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatar_file_path')
    avatar_url = models.URLField(max_length=400, blank=True, null=True)
    email = models.EmailField(unique=True, db_index=True, null=True)
    phone_no = models.CharField(max_length=50, null=True, unique=True)
    first_name = models.CharField(max_length=120, blank=True)
    last_name = models.CharField(max_length=120, blank=True)
    is_admin = models.BooleanField('admin', default=False)
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=(
            'Designates whether the q can log into this admin site.'
        ),
    )

    is_doctor = models.BooleanField(('staff status'),
        default=False,
        help_text=(
            'Designates whether the q can log into this admin site.'
        ),)

    date_joined = models.DateTimeField(
        ('date joined'), default=timezone.now
    )
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    ordering = ('created',)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Relatives(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_user')
    relative = models.ForeignKey(User, on_delete=models.CASCADE, related_name='relative_user')
    created_at = models.DateTimeField(auto_now=True)
