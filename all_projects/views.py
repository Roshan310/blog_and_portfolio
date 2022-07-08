from django.shortcuts import render
from .models import Project
# Create your views here.

def project_index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request , 'portfolio.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'project.html', context)