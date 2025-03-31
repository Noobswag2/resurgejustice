from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

from django.shortcuts import render

def team(request):
    return render(request, 'team.html')

from django.shortcuts import render

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    return render(request, 'profile.html')

def job_listings(request):
    return render(request, 'job_listings.html')

def mentor(request):
    return render(request, 'mentor.html')

def company(request):
    return render(request, 'company.html')
