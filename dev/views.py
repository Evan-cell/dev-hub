from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def project(request,pk):
    context = {}
    return render(request, 'single-project.html' , context)

def projects(request):
    context = {}
    return render(request, 'projects.html' , context)    

    
