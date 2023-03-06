import uuid
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, name, password, **other_fields)

    def create_user(self, email, name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user

# class PersonalInfo(models.Model):
#     email = models.EmailField(_('email address'), unique=True)
#     name = models.CharField(max_length=150)
#     mobile = models.CharField(max_length=150, blank=True)
#     images = models.ImageField(null=True, blank=True, upload_to='media')
#     # Address
#     city = models.CharField(max_length=50, verbose_name="Qaysi shaharda yashaysiz?",help_text="Hozirda yashaydigan mazilingizni ko'rsating")
#     street = models.CharField(max_length=50, verbose_name="Qaysi mahallada yashaysiz?", help_text="Hozirda yashaydigan mahalla yoki ko'changiz nomini kiriting")
#
#     # User Status
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     objects = CustomAccountManager()
#
#
#
#     class Meta:
#         verbose_name = "Accounts"
#         verbose_name_plural = "Accounts"


class Patsient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=150, blank=True)
    images = models.ImageField(null=True, blank=True, upload_to='media')
    password = models.CharField(max_length=50, null=False,blank=False)
    # Address
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name="Qaysi shaharda yashaysiz?",
                            help_text="Hozirda yashaydigan mazilingizni ko'rsating")
    street = models.CharField(max_length=50, null=True, blank=True, verbose_name="Qaysi mahallada yashaysiz?",
                              help_text="Hozirda yashaydigan mahalla yoki ko'changiz nomini kiriting")

    # User Status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class Nurse(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=150, blank=True)
    images = models.ImageField(null=True, blank=True, upload_to='media')
    password = models.CharField(max_length=50, null=False,blank=False)

    # Address
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name="Qaysi shaharda yashaysiz?",
                            help_text="Hozirda yashaydigan mazilingizni ko'rsating")
    street = models.CharField(max_length=50, null=True, blank=True, verbose_name="Qaysi mahallada yashaysiz?",
                              help_text="Hozirda yashaydigan mahalla yoki ko'changiz nomini kiriting")

    # User Status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    patsient = models.ForeignKey(Patsient, on_delete=models.SET_NULL, blank=True, null=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=150, blank=True)
    images = models.ImageField(null=True, blank=True, upload_to='media')
    password = models.CharField(max_length=50, null=False,blank=False)

    # Address
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name="Qaysi shaharda yashaysiz?",
                            help_text="Hozirda yashaydigan mazilingizni ko'rsating")
    street = models.CharField(max_length=50, null=True, blank=True, verbose_name="Qaysi mahallada yashaysiz?",
                              help_text="Hozirda yashaydigan mahalla yoki ko'changiz nomini kiriting")
    # User Status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, blank=True, null=True)
    patsient = models.ForeignKey(Patsient, on_delete=models.RESTRICT, blank=True, null=True)
    message = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name


class SeniorDoctor(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=150, blank=True)
    images = models.ImageField(null=True, blank=True, upload_to='media')
    password = models.CharField(max_length=50, null=False, blank=False)

    # Address
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name="Qaysi shaharda yashaysiz?",
                            help_text="Hozirda yashaydigan mazilingizni ko'rsating")
    street = models.CharField(max_length=50, null=True, blank=True, verbose_name="Qaysi mahallada yashaysiz?",
                              help_text="Hozirda yashaydigan mahalla yoki ko'changiz nomini kiriting")
    # User Status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True)
    nurse = models.ForeignKey(Nurse,  on_delete=models.SET_NULL,blank=True, null=True)
    patsient = models.ForeignKey(Patsient,  on_delete=models.SET_NULL, blank=True, null=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Admin(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=150, blank=True)
    images = models.ImageField(null=True, blank=True, upload_to='media')
    password = models.CharField(max_length=50, null=False,blank=False)

    # Address
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name="Qaysi shaharda yashaysiz?",
                            help_text="Hozirda yashaydigan mazilingizni ko'rsating")
    street = models.CharField(max_length=50, null=True, blank=True, verbose_name="Qaysi mahallada yashaysiz?",
                              help_text="Hozirda yashaydigan mahalla yoki ko'changiz nomini kiriting")
    # User Status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()
    senior_doctor = models.ForeignKey(SeniorDoctor,  on_delete=models.SET_NULL, blank=True, null=True)
    doctor = models.ForeignKey(Doctor,  on_delete=models.SET_NULL, blank=True, null=True)
    nurse = models.ForeignKey(Nurse,  on_delete=models.SET_NULL, blank=True, null=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        name = "Admin"
        return name

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, unique=True)
    img = models.ImageField(upload_to='profile_pict', null=True, blank=True)
    info = models.CharField(max_length=2000, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username