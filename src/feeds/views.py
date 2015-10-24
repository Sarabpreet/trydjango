from django.shortcuts import render

# Create your views here.
def home(request):
		return render(request,"home.html",{})

def resume(request):
		return render(request,"resume.html",{})

def home1(request):
		return render(request,"home1.html",{})
