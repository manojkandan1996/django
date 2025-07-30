from django.shortcuts import render
from django.http import HttpResponse

 
# Create your views here.
from .models import Project, Skill

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/about.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def contact(request):
    return render(request, 'portfolio/contact.html')
