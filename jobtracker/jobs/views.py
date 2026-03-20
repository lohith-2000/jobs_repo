from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm
from .filters import JobFilter
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def job_list(request):
    jobs = Job.objects.all()
    job_filter = JobFilter(request.GET, queryset=jobs)
    filtered_jobs = job_filter.qs

    paginator = Paginator(filtered_jobs, 10)
    page = request.GET.get('page')
    jobs = paginator.get_page(page)
    return render(request, 'jobs/job_list.html', {'jobs': jobs,'filter': job_filter})

@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)   # don't save yet
            job.user = request.user         # assign logged in user
            job.save()                      # now save

            form = JobForm()

            return render(request, 'jobs/add_job.html',
                          {'form': form, 'message': 'Job Saved Successfully'})
    else:
        form = JobForm()

    return render(request, 'jobs/add_job.html', {'form': form})
def edit_job(request, id):
    job = Job.objects.get(id=id)
    form = JobForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        return redirect('job_list')
    return render(request, 'jobs/edit_job.html', {'form': form})

def delete_job(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    return redirect('job_list')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})

