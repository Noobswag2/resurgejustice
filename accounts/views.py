from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile, Job
from .forms import UserProfileForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'accounts/profile.html', {'form': form, 'profile': profile})

@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'profile.html', {
        'form': form,
        'profile': profile
    })

def team(request):
    return render(request, 'team.html')

def about(request):
    return render(request, 'about.html')

def job_listings(request):
    jobs = Job.objects.all().order_by('-posted_at')
    return render(request, 'job_listings.html', {'jobs': jobs})

from .forms import ApplicationForm

def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'apply_success.html')  # A simple thank you page
    else:
        form = ApplicationForm()
    return render(request, 'apply.html', {'form': form})

from .forms import MentorRequestForm

def connect_mentor(request, mentor_name):
    if request.method == 'POST':
        form = MentorRequestForm(request.POST)
        if form.is_valid():
            mentor_request = form.save(commit=False)
            mentor_request.mentor_name = mentor_name
            mentor_request.save()
            return render(request, 'connect_success.html', {'mentor_name': mentor_name})
    else:
        form = MentorRequestForm()

    return render(request, 'connect_mentor.html', {'form': form, 'mentor_name': mentor_name})

from .forms import ApplicationForm

@login_required(login_url='/accounts/login/')
def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'apply_success.html')
    else:
        form = ApplicationForm()
    return render(request, 'apply.html', {'form': form})
