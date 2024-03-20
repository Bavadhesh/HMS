from django.shortcuts import render, redirect
from .models import Patient, Login

def patient_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        mobile_no = request.POST.get('mobile_no')
        email = request.POST.get('email')
        address = request.POST.get('address')
        profile_photo = request.FILES.get('profile_photo')
        
        print(request.FILES.get('profile_photo'))
        password = request.POST.get('password')

        # Get the last patient ID from the database
        last_patient = Patient.objects.last()
        last_id = last_patient.id if last_patient else 999

        # Increment the ID by one for the new patient
        new_id = last_id + 1

        # Create a new Patient object and save it to the database
        patient = Patient(
            id=new_id,
            name=name,
            age=age,
            mobile_no=mobile_no,
            email_id=email,
            address=address,
            profile_photo=profile_photo
        )
        patient.save()

        # Create a new Login object and save it to the database
        login = Login(
            id=new_id,
            email=email,
            password=password,
            usertype = "patient"
        )
        login.save()
       
        # return render(request,'login.html',{'error_message': "Registration successful"})
        return redirect('/login')

       

    return render(request,'Patient_Register.html')
