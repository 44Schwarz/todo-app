from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {}
    return render(request, 'tasks/index.html', context)


def all_projects(request):
    return HttpResponse('All your projects')


def detail(request, project_id):
    return HttpResponse('Project #{}'.format(project_id))
