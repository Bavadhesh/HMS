from django.shortcuts import render, get_object_or_404,redirect
from .models import Doctor, Patient,Prescription
import os
from pathlib import Path

def diagnose_patient(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        doctor_id = request.session.get('doctor_id')
        doctor = get_object_or_404(Doctor, id=doctor_id)
        print(doctor)
        patient = get_object_or_404(Patient, id=patient_id)
        request.session['patient_id']=patient.id

        # Perform the diagnosis process here
        # ...

        context = {
            'doctor': doctor,
            'patient': patient,
            # Add any additional context data required for the diagnosis process
        }

        return render(request, 'diagnose.html', context)

    return render(request, 'DoctorDiagonosePatient.html')

def prescription(request):
    patient = get_object_or_404(Patient, id=request.session.get('patient_id'))
    old_prescription = Prescription.objects.filter(patient=patient)
    print(old_prescription)
    context = {
        'oldPrescription':old_prescription
    }
    return  render(request,'UploadPrescription.html',context)  

def Patient_prescription(request):
    patient = get_object_or_404(Patient, id=request.session.get('patient_id'))
    old_prescription = Prescription.objects.filter(patient=patient)
    print(old_prescription)
    context = {
        'oldPrescription':old_prescription
    }
    return  render(request,'Prescriptions.html',context)  


def upload_prescription(request):
    doctor_id = request.session.get('doctor_id')
    doctor = get_object_or_404(Doctor, id=doctor_id)
    patient_id = request.session.get('patient_id')
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        # Assuming the prescription file is uploaded as 'prescription_file' in the form
        prescription_file = request.FILES.get('prescription_file')

        # Save the prescription file and create a Prescription object
        prescription = Prescription(patient=patient, doctor=doctor, document = prescription_file)
        prescription.save()

        # Perform any additional operations or redirect to a success page
    patient = get_object_or_404(Patient, id=request.session.get('patient_id'))
    old_prescription = Prescription.objects.filter(patient = patient)
    
    print(old_prescription)
    
    context = {
        'doctor': doctor,
        'patient': patient,
        'oldPrescription':old_prescription
    }

    return  render(request,'UploadPrescription.html',context)  

from django.http import FileResponse,HttpResponse

def view_prescription(request,file_path):
    try:
       
        BASE_DIR = Path(__file__).resolve().parent.parent
        # Assuming the prescription_file field is a FileField or FilePathField
        prescription_file =  os.path.join(BASE_DIR,'hms','media','prescriptions',file_path)
        
        # Open the file and create a FileResponse
        file = open(prescription_file, 'rb')  # Open the file in binary mode for reading
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response

    except Patient.DoesNotExist:
        # Handle the case when the patient is not found
        return HttpResponse('Patient not found.', status=404)
    except Prescription.DoesNotExist:
        # Handle the case when the prescription is not found
        return HttpResponse('Prescription not found.', status=404)

def view_report(request,file_path):
    try:
       
        BASE_DIR = Path(__file__).resolve().parent.parent
        # Assuming the prescription_file field is a FileField or FilePathField
        prescription_file =  os.path.join(BASE_DIR,'hms','media','diagnosis_reports',file_path)
        
        # Open the file and create a FileResponse
        file = open(prescription_file, 'rb')  # Open the file in binary mode for reading
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response

    except Patient.DoesNotExist:
        # Handle the case when the patient is not found
        return HttpResponse('Patient not found.', status=404)
    except Prescription.DoesNotExist:
        # Handle the case when the prescription is not found
        return HttpResponse('Prescription not found.', status=404)
