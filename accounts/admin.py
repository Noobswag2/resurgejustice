from django.contrib import admin
from .models import UserProfile, Job
from .models import Company

admin.site.register(UserProfile)
admin.site.register(Job)
admin.site.register(Company)