from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectslist = [
    {
        'id':1,
        'title':'Ecommerce Website',
        'description':'Fully Functional ecommerce website'
    },
    {
        'id':2,
        'title':'Portfolio Website',
        'description':'This was a project where I built my own portfolio'
    },
    {
        'id':3,
        'title':'Social Network',
        'description':'Awesome open source project I am still working on. '
    },
]

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
    a = None
    for dic_item in projectslist:
        if dic_item['id'] == int(pk):
            a = dic_item

    context = {'message': 'Test', 'pk':pk, 'projects': projectslist, 'project':a}
    return render(request, 'projects/test.html', context)