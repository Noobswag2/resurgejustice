from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import profile_view

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('team/', views.team, name='team'),
    path('about/', views.about, name='about'),
    path('job-listings/', views.job_listings, name='job_listings'),
    path('apply/', views.apply, name='apply'),
    path('connect/<str:mentor_name>/', views.connect_mentor, name='connect_mentor')
]
