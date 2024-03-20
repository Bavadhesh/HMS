"""hms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,re_path
from HospitalManagementSystem import Doctor_profile, views,Patient_Registration,Patient_Login,Patient_LandingPage,Appointments,Diagonose,LT_profile,PatientDiagonosisreports

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Patient_Login.land),
    path('patient/register/',Patient_Registration.patient_registration),
    path('login/',Patient_Login.user_login),
    path('login/patient/auth/',Patient_LandingPage.patient_profile),
    path('logout/',Patient_Login.logout_view),
    path('login/patient/auth/prescriptions/',Diagonose.Patient_prescription),
    re_path(r'.*?/reports/$',PatientDiagonosisreports.patient_reports),
    re_path(r'login/patient/auth//[^/]+/logout/',Patient_Login.logout_view),
    re_path(r'^login/doctor/auth/.*?/prescriptions/$',Diagonose.prescription),
    re_path(r'^login/patient/auth/.*?/appointments/$',Appointments.load_patient_appointments),
    path('login/patient/auth/appointments/',Appointments.load_patient_appointments),
    path('login/doctor/auth/',Doctor_profile.doctor_details),
    path('login/doctor/auth/appointments/',Appointments.doctor_appointments),
    path('login/doctor/auth/diagonose/',Diagonose.diagnose_patient),
    path('login/doctor/auth/diagonose/prescription/',Diagonose.prescription),
    path('login/doctor/auth/diagonose/prescription/uploadPrescription',Diagonose.upload_prescription),
    re_path(r'^login/doctor/auth/.*?/uploadPrescription/$',Diagonose.upload_prescription),
    re_path(r'^login/doctor/auth/diagonose/.*?/prescription/$',Diagonose.prescription),
    re_path(r'^login/doctor/auth/.*?/appointments/$',Appointments.doctor_appointments),
    re_path(r'^login/doctor/auth/.*?/diagonose/$',Diagonose.diagnose_patient),
    path('prescriptions/<str:file_path>/',Diagonose.view_prescription),
    path('diagnosis_reports/<str:file_path>/',Diagonose.view_report),
    path('login/LT/auth/',LT_profile.lab_technologist_profile),
    path('login/LT/auth/ReportUpload/',LT_profile.upload_diagnosis_report),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
