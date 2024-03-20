from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request,'HC/HC_main_page.html')