from django.contrib import admin
from .models import Nurse,Patsient, Doctor,SeniorDoctor,Admin, Profile
# Register your models here.




admin.site.register(Profile)




@admin.register(Patsient)
class Patsient(admin.ModelAdmin):
    list_display = ['user',
                    'name',
                    'email',
                    'mobile',
                    'images',
                    'city',
                    'street',
                    'is_staff',
                    'is_active',
                    ]
    # list_filter = ['in_stock', 'is_active']


@admin.register(Nurse)
class Nurse(admin.ModelAdmin):
    list_display = ['name',
                    'email',
                    'mobile',
                    'images',
                    'city',
                    'street',
                    'is_staff',
                    'is_active',
                    'patsient']
    # list_filter = ['in_stock', 'is_active']

@admin.register(Doctor)
class Doctor(admin.ModelAdmin):
    list_display = ['name',
                    'email',
                    'mobile',
                    'images',
                    'city',
                    'street',
                    'is_staff',
                    'is_active',
                    'patsient',
                    'nurse']
    # list_filter = ['in_stock', 'is_active']


@admin.register(SeniorDoctor)
class SeniorDoctor(admin.ModelAdmin):
    list_display = ['name',
                    'email',
                    'mobile',
                    'images',
                    'city',
                    'street',
                    'is_staff',
                    'is_active',
                    'patsient',
                    'nurse',
                    'doctor']


@admin.register(Admin)
class Admin(admin.ModelAdmin):
    list_display = ['name',
                    'email',
                    'mobile',
                    'images',
                    'city',
                    'street',
                    'is_staff',
                    'is_active',
                    'nurse',
                    'doctor']