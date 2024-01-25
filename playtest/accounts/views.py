from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from .forms import CreateUserForm, UserForm
from django.http import HttpResponse
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy




@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create the user instance without saving to the database yet
            user.is_active = True  # Set the is_active attribute
            user.save()  # Save the user instance to the database
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect.')

    context = {}
    return render(request, 'accounts/login.html', context)



@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserForm(instance=user)

    return render(request, 'accounts/profile.html', {'form': form})


@login_required
def user_profile(request):
    return render(request, 'accounts/userprofile.html')

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserForm(instance=user)

    return render(request, 'accounts/edit_profile.html', {'form': form})


    return render(request, 'accounts/edit_profile.html', {'form': form})
@login_required
class ChangePasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('change_password_done')
@login_required
class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = 'accounts/change_password_done.html'

