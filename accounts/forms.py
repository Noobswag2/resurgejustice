from django import forms
from .models import UserProfile 

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['academic_education', 'non_formal_education', 'experience', 'certifications']  
