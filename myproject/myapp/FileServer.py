from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Patient_Documents
from django.contrib.auth import authenticate,login
import mimetypes
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def DiagonosisReport(request):
     
     patient_documents = Patient_Documents.objects.filter(patient_id=request.session["id"], DocumentType = 'DR')
     DocumentList = {
          "ID":request.session["id"],
          "Documents":patient_documents,
     }
     return render(request,'myapp/DiagonosisReport.html',DocumentList) 

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def Prescriptions(request):
     
     patient_documents = Patient_Documents.objects.filter(patient_id=request.session["id"], DocumentType = 'P')
     DocumentList = {
          "ID":request.session["id"],
          "Documents":patient_documents
     }
     return render(request,'myapp/Prescriptions.html',DocumentList)    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def DownloadAndView(request,id,FileName):
      docpath = "C:\\Users\\Bavadhesh\\Desktop\\P01\\myproject\\myproject\\static\\upload\\Documents\\"+FileName
      print(docpath)
      
    # Open the file for reading content
      path = open(docpath, 'rb')
    # Set the mime type
      mime_type, _ = mimetypes.guess_type(docpath)
    # Set the return value of the HttpResponse
      response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
      response['Content-Disposition'] = "attachment; filename=%s" % FileName
    # Return the response value
      return response
     