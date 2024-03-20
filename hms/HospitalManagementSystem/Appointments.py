from django.shortcuts import render, get_object_or_404
from .models import Doctor, Appointment,Patient

def doctor_appointments(request):
    # Retrieve the doctor object based on the logged-in user's session data
    doctor_id = request.session.get('doctor_id')
    doctor = get_object_or_404(Doctor, id=doctor_id)

    # Retrieve the appointments of the doctor
    appointments = Appointment.objects.filter(doctor=doctor)

    print(appointments)

    # Pass the doctor and appointments to the template for rendering
    context = {
        'doctor': doctor,
        'appointments': appointments,
    }

    return render(request, 'Doctor_appointment.html', context)

def load_patient_appointments(request):
    # Get the patient ID from the session
    patient_id = request.session.get('patient_id')
    patient = get_object_or_404(Patient, id=patient_id)

    # Query the appointments for the patient
    appointments = Appointment.objects.filter(patient=patient)

    context = {
        'appointments': appointments
    }

    return render(request, 'patient_appointments.html', context)