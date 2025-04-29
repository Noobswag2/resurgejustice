from django import forms
from .models import UserProfile 

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['academic_education', 'non_formal_education', 'experience', 'certifications']  

from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'email', 'phone', 'message']

from django import forms
from .models import MentorRequest

class MentorRequestForm(forms.ModelForm):
    class Meta:
        model = MentorRequest
        fields = ['full_name', 'email', 'phone', 'message']
