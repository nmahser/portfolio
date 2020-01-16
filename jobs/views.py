from django.shortcuts import render, redirect, get_object_or_404
from jobs.models import Job

# Create your views here.


'''
def home(request):
    jobs = Job.objects
    # You should render child template not the parent!
    return render(request, 'contact.html', {'jobs': jobs})
'''


def detail(request, job_id):
    jobDetail = get_object_or_404(Job, pk=job_id)
    return render(request, 'detail.html', {'job': jobDetail})
