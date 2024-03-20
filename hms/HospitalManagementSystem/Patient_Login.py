from django.shortcuts import render, redirect
from .models import Login, Patient, Doctor, LabTechnologist
from django.http import HttpResponse

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Retrieve the Login entry based on the provided email and password
        login_entry = Login.objects.filter(email=email, password=password).first()
        print(login_entry)

        if login_entry:
            # Set the user type based on the Login entry
            user_type = login_entry.usertype

            # Set the appropriate session data based on the user type
            request.session['user_type'] = user_type

            # Redirect to the appropriate dashboard or desired page based on the user type
            if user_type == 'patient':
                patient = Patient.objects.get(id=login_entry.id)
                print(patient)
                request.session['patient_id'] = patient.id
                return redirect('patient/auth/')
            elif user_type == 'doctor':
                doctor = Doctor.objects.get(id=login_entry.id)
                request.session['doctor_id'] = doctor.id
                return redirect('doctor/auth')
            elif user_type == 'labtechnologist':
                lab_technologist = LabTechnologist.objects.get(id=login_entry.id)
                request.session['lab_technologist_id'] = lab_technologist.id
                return redirect('LT/auth')
        else:
            # Invalid credentials, display an error message
            error_message = "Invalid email or password. Please try again."
            print(error_message)
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def logout_view(request):
    # Clear session data
    request.session.flush()
    return redirect('/login/')  # Redirect to the desired page after logout

def land(request):
    return render(request,'landingPage.html')