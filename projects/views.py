from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def projects(request):
    projects = Project.objects.all()
    
    context = {'projects':projects }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    #tags = projectObj.tags.all()            
    return render(request, 'projects/single-project.html', {'project':projectObj})

def test(request, pk):
    context = {'message': 'Test', 'pk':pk, 'projects':1, 'project':1}
    return render(request, 'projects/test.html', context)

@login_required(login_url='login')
def createproject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {"form":form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateproject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {"form":form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteproject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method =='POST':
        project.delete()
        return redirect('projects')
    context ={'object':project}
    return render(request, 'projects/delete_template.html', context)