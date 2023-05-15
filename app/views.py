from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import django_filters
from accounts.forms import ProfileForm
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from employer.models import Job
from employer.filters import JobFilter
from jobseeker.models import Person, Application
from accounts.models import Profile

# check if prfofle.user_type before accessing the page
def getUserType(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            if profile.user_type == 'JS':
                request.session['user_type'] = 'JS'
                return redirect('jobseeker_home')
            else:
                request.session['user_type'] = 'RC'
                return redirect('employer_home')
        except Profile.DoesNotExist:
            return redirect('create_profile')
    else:
        return redirect('account_login')


# Create your views here.
@login_required
def landing(request):
    try:
        print('checking profile')
        profile = Profile.objects.filter(user=request.user).first()
        print(profile)
        if profile is not None:
            request.session['user_type'] = profile.user_type
            if profile.user_type == 'JS':
                return redirect('index')
            else:
                return redirect('applicants')
        else:
            return redirect('create_profile')
    except Exception as e:
        print(e)
        return redirect('create_profile')
    return render(request, 'landing.html')

def contactus(request):
    return render(request, 'contactus.html')

def about(request):
    return render(request, 'about.html')

@login_required
def index(request):
    getUserType(request)
    jobs = Job.objects.all()
    job_filter = JobFilter(request.GET, queryset=jobs)
    applications = Application.objects.filter(person__user=request.user)
    print(applications)
    ctx = {
        'job_filter': job_filter,
        'job_applied': applications,
    }
    return render(request, 'index.html', ctx)
@login_required
def dashboard(request):
    # check if user has a profile set
    try:
        profile = Profile.objects.get(user=request.user)
        return redirect('/jobseeker/home/')
    except Profile.DoesNotExist:
        return redirect('/accounts/profile/create')


@login_required
def job(request, id):
    job = get_object_or_404(Job, pk=id)
    ctx = {
        'job': job,
    }
    return render(request, 'job.html', ctx)

@login_required
def apply_job(request, id):
    if request.session['user_type'] != 'JS':
        messages.error(request, 'You are not authorized to access this page.')
        return redirect('index')
    job = get_object_or_404(Job, pk=id)
    if request.method == 'POST':
        # check if person exists
        try:
            person = Person.objects.filter(user=request.user).first()
            # check if application exists
            try:
                if person is not None:
                    application = Application.objects.get(job=job, person=person)
                    messages.error(request, 'You have already applied for this job.')
                    print('already applied')
                    return redirect('job', id=id)
                else:
                    return redirect('jobseeker_home')
            except Application.DoesNotExist:
                    application = Application.objects.create(job=job, person=person)
                    messages.success(request, 'You have successfully applied for the job.')
                    print('applied')
                    return redirect('job', id=id)
        except Person.DoesNotExist:
            messages.error(request, 'You need to create a profile to apply for a job.')
            return redirect('jobseeker_home')
    else:
        messages.error(request, 'Something went wrong. Please try again.')
        return redirect('job', id=id)
