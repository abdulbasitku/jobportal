from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Job

# Create your views here.
def home(request):
    all_jobs = Job.objects
    return render(request, 'jobs/home.html',{'all_jobs':all_jobs})


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})