from django.shortcuts import render, redirect
from .forms import ContactForm  

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

def mentor(request):
    return render(request, 'mentor.html')

def company(request):
    return render(request, 'company.html')
