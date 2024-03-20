from django.shortcuts import render,redirect
from .models import LabTechnologist,DiagnosisReport,Patient,Doctor
from django.http import HttpResponse
from datetime import date


def lab_technologist_profile(request):
    # Get the user ID from the session
    lab_technologist_id = request.session.get('lab_technologist_id')

    try:
        # Query the LabTechnologist model for the user
        lab_technologist = LabTechnologist.objects.get(id=lab_technologist_id)
        print(lab_technologist.profile_photo)
    except LabTechnologist.DoesNotExist:
       
        # Handle the case when the LabTechnologist is not found
        return HttpResponse("Lab Technologist not found")

    context = {
        'lab_technologist': lab_technologist
    }

    return render(request, 'Lab_profile.html', context)

def ReportUpload(request):
    return render(request,'Report_upload.html')



def upload_diagnosis_report(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        patient_id = request.POST.get('patient_id')
        doctor_id = request.POST.get('doctor_id')
        report_file = request.FILES.get('report_file')

        patient = Patient.objects.get(id=patient_id)
        doctor = Doctor.objects.get(id=doctor_id)
        lab_technologist = LabTechnologist.objects.get(id=request.session.get('lab_technologist_id'))

        # Create a new instance of the DiagnosisReport model
        report = DiagnosisReport(patient=patient, doctor=doctor,report_date=date.today(),report_file=report_file)
        # Set the lab technologist based on the logged-in user
       
        report.save()
        return HttpResponse("<script>alert('successful')</script>")

    return render(request, 'Report_upload.html')
       
