from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm   
from django.contrib import messages

# Create your views here.

def home(request):
    # add person form
    form = PersonForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            person=form.save(commit=False) # save the form data to model
            person.user = request.user # assign the current logged in user to the model
            person.save() # save the model to the database
            messages.success(request, 'Your details added successfully')
            return redirect('jobseeker_home')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'jobseeker/jobseeker_home.html', ctx)