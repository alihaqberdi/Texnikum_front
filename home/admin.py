from django.contrib import admin

from . models import *

admin.site.register([Video, VideoCategorie])

@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = 'name',
    search_fields = 'name',
    list_filter = 'name',

@admin.register(LeaderDoctor)
class LeaderDoctorAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.user_type == 'doctor_leader':
            queryset = queryset.filter(clinica=request.user.clinica)
        return queryset


    list_display = 'full_name', 'user', 'clinica'
    search_fields = 'full_name',
    list_filter = 'clinica',

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = 'full_name', 'user', 'clinica', 'leader_doctor'
    search_fields = 'full_name',
    list_filter = 'clinica',

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = 'full_name', 'user', 'clinica', 'doctor'
    search_fields = 'full_name',
    list_filter = 'clinica', 'doctor'