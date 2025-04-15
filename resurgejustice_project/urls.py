from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('jobs/', views.job_listings, name='job_listings'),
    path('mentor/', views.mentor, name='mentor'),
    path('company/', views.company, name='company'),
    path('accounts/', include('accounts.urls')),
]
