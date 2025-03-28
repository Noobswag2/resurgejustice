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
