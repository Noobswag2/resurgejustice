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
    # path('profile/suggestions/', views.get_profile_suggestions, name='profile_suggestions'),
]
