from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm,ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# # Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Rediriger vers une page de confirmation ou de connexion
            return redirect('signIn')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signUp.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = ''
    return render(request, 'signIn.html', {'error_message': error_message})


def logout_view(request):
    logout(request)
    messages.success(request,("You have been logout"))
    return redirect('home')


@login_required
def profile_update(request):
    user = request.user
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
    else:
        profile_form = ProfileUpdateForm(instance=user.profile)
    return render(request, 'profile_update.html', {'profile_form': profile_form})

def profile_detail(request):
    profile = request.user.profile
    return render(request, 'profile_detail.html', {'profile': profile})