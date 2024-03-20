from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from myapp.models import Patients,Treatmentplan
from django.contrib.auth import authenticate,login
from django.views.decorators.cache import cache_control
from django.core.cache import cache 

def Landing(request):
     return render(request,'myapp/landingPage.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def register(request):
    p = {
                'problem':False,
                'problemStatement':''
           }
    if request.method == 'POST':
           
           Patient = Patients()
           
           Patient.Patient_Id = Patients.objects.last().Patient_Id + 1
           
           Patient.FirstName = request.POST['FirstName']
           Patient.LastName = request.POST['LastName']
           Patient.Age = request.POST['Age']
           Patient.MobileNumber =  request.POST['MobileNumber']
           Patient.profile_photo = request.FILES.get('Profile_photo')
           Patient.CareTakerName =  request.POST['CareTakerName']
           Patient.CareTakerMobileNumber =  request.POST['CareTakerMobileNumber']
           Patient.EmailId = request.POST['EmailId']
           Patient.Address =  request.POST['Address']
           Patient.password1 = request.POST['Password1']
           Patient.password2 = request.POST['Password2']
           EmailCheck = Patient.EmailId.split("@")
           
           if len(EmailCheck) != 2:
                p = {
                'problem':True,
                'problemStatement':'Invalid Email'
                     }
                 
                return render(request,'myapp/Register.html',p)
           if Patient.password1 != Patient.password2:
                p = {
                'problem':True,
                'problemStatement':'Password Not Matching'
                     }
                 
                return render(request,'myapp/Register.html',p)
           if Patients.objects.filter(EmailId=Patient.EmailId).exists()==True :
                p = {
                'problem':True,
                'problemStatement':'Email Id already exists'
                     }
                 
                return render(request,'myapp/Register.html',p) 
           
           Patient.save()
    else:
        return render(request,'myapp/Register.html',p) 
    return render(request,'myapp/regsuccess.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)        
def login(request):
    
     p = {
                'problem':False,
                'problemStatement':''
           }
     if request.method == 'POST':
         
          request.session["Authenticated"] = True
          if Patients.objects.filter(EmailId=request.POST['Email']).exists()==True:
               Patient = Patients.objects.get(EmailId=request.POST['Email'])
               if(Patient.password1!=request.POST['Password']):
                    p = {
                      'problem':True,
                       'problemStatement':'Wrong Password'
                    }
                    return render(request,'myapp/login.html',p)  
               else:
                    request.session["id"] = Patient.Patient_Id
                    
                    if request.session["Authenticated"] == True :
                       profile = {
                         'Name':Patient.FirstName + " " + Patient.LastName,
                         'Age':Patient.Age,
                         'ID':Patient.Patient_Id,
                         'MNo':Patient.MobileNumber,
                         'Address':Patient.Address,
                         'Profile_Photo':Patient.profile_photo,
                         'Care_taker':Patient.CareTakerName,
                         'Care_taker_Mno': Patient.CareTakerMobileNumber,
                         }
                       return render(request,'myapp/patient.html',profile)
          else:
              p = {
                      'problem':True,
                       'problemStatement':'Email not exists'
                    }    
              return render(request,'myapp/login.html',p)

     else:
          return render(request,'myapp/login.html',p)  

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def TreatmentPlan(request):
     print(id)
     Schedule = Treatmentplan.objects.filter(patient_id = request.session["id"])
     print(Schedule)
     ScheduleList = {
          'ID':request.session["id"],
          'Schedule':Schedule,
     }
     return render(request,'myapp/TreatmentPlan.html',ScheduleList)   

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def Logout(request):
     del request.session
     return redirect('/login')

