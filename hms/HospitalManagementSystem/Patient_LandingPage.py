from django.shortcuts import render, get_object_or_404
from .models import Patient

def patient_profile(request):
    # Retrieve the patient object based on the logged-in user's session data
    patient_id = request.session.get('patient_id')
    patient = get_object_or_404(Patient, id=patient_id)
    print(patient.profile_photo)
    # Pass the patient object to the template for rendering
    context = {
        'patient': patient,
    }

    return render(request, 'patient_profile.html', context)