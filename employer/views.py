from django.shortcuts import render, redirect
from .models import Person as Employer
from .models import Job
from jobseeker.models import Application, Person
from accounts.models import Profile
from .forms import PersonForm   
from django.contrib import messages
from .filters import ApplicationFilter
from jobseeker.forms import JobForm

def home(request):
    # add person form
    form = PersonForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            emp = form.save(commit=False) # save the form data to model
            emp.user = request.user # add the user
            emp.save() # save the model
            messages.success(request, 'Your details added successfully')
            return redirect('employer_home')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'employer/employer_home.html', ctx)

def jobdesc(request):
    return (request,'employer/jobdesc.html')

def applicants(request):
    # if person profile is set
    try:
        profile =Profile.objects.get(user=request.user)
        if profile.user_type == 'RC':
            # check if employer is available
            try:
                employer = Employer.objects.filter(user=request.user).first()
                print('employer', employer)
                if employer is not None:
                    # display all applications for this employer
                    print(request.user)
                    jobs = Job.objects.filter(user=request.user)
                    applications = Application.objects.filter(job__user=request.user)
                    appl_counts = applications.count()
                    ctx = {
                        'appl': applications,
                        'counts': appl_counts,
                        'jobs': jobs,
                    }
                    return render(request, 'employer/applicants.html', ctx)
            except Employer.DoesNotExist:
                messages.error(request, 'you have not filled the employer form')
                return redirect('employer_home')    
        else:
            messages.error(request, 'you are not an employer')
            return redirect('/')
    except Profile.DoesNotExist:
        messages.error(request, 'you have not filled the profile form')
        return redirect('create_profile')
    return render(request, 'employer/applicants.html')

def create_job(request):
    # if person profile is set
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False) # save the form data to model
            job.user = request.user # add the user    
            job.save() # save the model        
            messages.success(request, 'Your job added successfully')
            return redirect('employer_home')
        else:
            messages.error(request, 'Error adding your job')
    else:
        form = JobForm()
    ctx = {'form': form}
    return render(request, 'employer/jobform.html', ctx)

def accept(request, id):
    applicant = Application.objects.get(id=id)
    applicant.accepted = True
    applicant.save()
    messages.success(request, 'Applicant accepted')
    return redirect('applicants')

def reject(request, id):
    applicant = Application.objects.get(id=id)
    applicant.accepted = False
    applicant.save()
    messages.success(request, 'Applicant rejected')
    return redirect('applicants')

def delete_job(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    messages.success(request, 'Job deleted')
    return redirect('applicants')