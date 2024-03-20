from django.db import models

# Create your models here.
class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile_no = models.CharField(max_length=20)
    email_id = models.EmailField()
    address = models.TextField()
    profile_photo = models.ImageField(upload_to='patient_profiles/')

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    designation = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)
    address = models.TextField()
    email_id = models.EmailField()
    profile_photo = models.ImageField(upload_to='doctor_profiles/')

    def __str__(self):
        return self.name
    
class LabTechnologist(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    designation = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)
    email_address = models.EmailField()
    address = models.TextField()
    profile_photo = models.ImageField(upload_to='lab_technologist_profiles/')

    def __str__(self):
        return self.name
    
class Prescription(models.Model):
    patient = models.ForeignKey('HospitalManagementSystem.Patient', on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey('HospitalManagementSystem.Doctor', on_delete=models.CASCADE, null=True)
    document = models.FileField(upload_to='prescriptions/')

    def __str__(self):
        if self.patient:
            return f"Prescription for {self.patient.name} by Dr. {self.doctor.name}"
        else:
            return f"Prescription by Dr. {self.doctor.name}"
        
class DiagnosisReport(models.Model):
    patient = models.ForeignKey('HospitalManagementSystem.Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('HospitalManagementSystem.Doctor', on_delete=models.CASCADE)
    report_date = models.DateField()
    report_file = models.FileField(upload_to='diagnosis_reports/')

    def __str__(self):
        return f"Diagnosis Report for {self.patient.name} by Dr. {self.doctor.name}"
    
class Appointment(models.Model):
    patient = models.ForeignKey('HospitalManagementSystem.Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('HospitalManagementSystem.Doctor', on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient.name} with Dr. {self.doctor.name} on {self.appointment_date} at {self.appointment_time}"

class Login(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    usertype = models.CharField(max_length=20)

    def __str__(self):
        return self.email