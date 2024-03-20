from django.shortcuts import render, redirect
from .models import Login, Doctor

def doctor_details(request):
    # Retrieve the doctor object based on the logged-in user's session data
    doctor_id = request.session.get('doctor_id')
    doctor = Doctor.objects.get(id=doctor_id)

    # Pass the doctor object to the template for rendering
    context = {
        'doctor': doctor,
    }

    return render(request, 'doctor_profile.html', context)
