from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    academic_education = models.TextField(blank=True)
    non_formal_education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    certifications = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
