from django.shortcuts import render
from django.http import HttpResponse
from .models import Job

# Create your views here.
def index(request):
    all_jobs = Job.objects
    return render(request, 'jobs/home.html',{'all_jobs':all_jobs})
