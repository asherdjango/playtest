from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username

class ChangePasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('change_password_done')

class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = 'accounts/change_password_done.html'



	

