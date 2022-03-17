from django.shortcuts import render

from .models import *

def branches(request):
    ctx = {
        'branches': Branche.objects.all()
    }
    return render(request, 'university/branches.html', ctx)

def faculties(request):
    ctx = {
        'faculties': Faculty.objects.all()
    }
    return render(request, 'university/faculties.html', ctx)

def courses(request):
    ctx = {
        'courses': Course.objects.all()
    }
    return render(request, 'university/courses.html', ctx)
