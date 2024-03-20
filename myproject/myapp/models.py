from django.db import models

# Create your models here.
class Patients(models.Model) :
    class Meta:
        db_table = 'Patients'
    Patient_Id = models.BigIntegerField(default=1000)
    FirstName = models.CharField(max_length = 100)
    LastName = models.CharField(max_length = 100)
    Age = models.IntegerField()
    MobileNumber = models.CharField(max_length=10)
    EmailId = models.CharField(max_length=100)
    CareTakerName = models.CharField(max_length=100)
    profile_photo = models.ImageField()
    CareTakerMobileNumber = models.CharField(max_length=10)
    Address = models.CharField(max_length=500)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

class Treatmentplan(models.Model):
    patient_id = models.BigIntegerField()  # Field name made lowercase.
    purpose = models.CharField(max_length=1000)
    date = models.DateField()  # Field name made lowercase.
    time = models.CharField(max_length = 50)  # Field name made lowercase.

    class Meta:
        
        db_table = 'treatmentplan'

class Patient_Documents(models.Model):
    patient_id = models.BigIntegerField()  # Field name made lowercase.
    uploaded_time = models.DateTimeField(auto_now_add=True)
    DocumentType = models.CharField(max_length = 50,default="")
    Document = models.FileField(upload_to='Documents/')
    class Meta:
        db_table = 'Patient_Documents'
                
    