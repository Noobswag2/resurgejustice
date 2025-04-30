from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from accounts.models import Company

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  
            return redirect('contact')  
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

def job_listings(request):
    return render(request, 'job_listings.html')

@login_required
def mentor(request):
    mentors = [
        {'name': 'John Doe', 'description': 'Experienced Software Engineer and Mentor', 'image': 'mentor1.jpeg'},
        {'name': 'Jane Smith', 'description': 'Career coach specializing in tech and startups', 'image': 'mentor2.jpeg'},
        {'name': 'Emily Johnson', 'description': 'Helping ex-cons transition into tech careers', 'image': 'mentor3.webp'},
        {'name': 'Dale Jackson', 'description': 'Helping ex-cons transition into corporate life',},
    ]
    return render(request, 'mentor.html', {'mentors': mentors})

def company(request):
    companies = Company.objects.all()[:5]  # Show first 5 companies
    return render(request, 'company.html', {'companies': companies})
