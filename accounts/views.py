from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages

@login_required
def index(request):
    try:
        profile = Profile.objects.get(user=request.user)
        ctx = {'profile': profile}
        return render(request, 'account/view_profile.html', ctx)
    except Profile.DoesNotExist:
        return redirect('/accounts/profile/create')
    

@login_required
def create_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if profile is not None:
        return redirect('update_profile')
    form = ProfileForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            return redirect('/')
    ctx = {'form': form}

    return render(request, 'account/create_profile.html', ctx)


@login_required
def update_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('/accounts/')
        ctx = {'form': form, 'profile': profile}
        return render(request, 'account/update_profile.html', ctx)
    except Profile.DoesNotExist:
        return redirect('/accounts/profile/create')
    
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
