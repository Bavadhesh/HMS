from django.contrib import admin
from .models import Patient,Doctor,LabTechnologist,Prescription,DiagnosisReport,Appointment,Login


# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(LabTechnologist)
admin.site.register(Prescription)
admin.site.register(DiagnosisReport)
admin.site.register(Appointment)
admin.site.register(Login)



