from django.urls import path
from . import views

urlpatterns = [
    # Your existing URL patterns
    
    
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),  # For editing the profile
    path('change_password/', views.ChangePasswordView, name='change_password'),  # For changing the password
    path('change_password_done/', views.ChangePasswordDoneView, name='change_password_done'),  # Password change done
]
