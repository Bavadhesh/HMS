from django.shortcuts import render
from .models import Patient, DiagnosisReport

def patient_reports(request):
    # Retrieve the patient object
    patient = Patient.objects.get(id=request.session.get("patient_id"))

    # Retrieve the diagnosis reports for the patient
    reports = DiagnosisReport.objects.filter(patient=patient)

    # Pass the patient and reports to the template for rendering
    context = {'patient': patient, 'reports': reports}
    return render(request, 'PatientDiagonosisReports.html', context)
