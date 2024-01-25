from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from accounts.views import logo
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'mainsite/home.html')

