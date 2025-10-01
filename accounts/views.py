from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm    
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import views
from .forms import CustomUserCreationForm

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                
                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            form = AuthenticationForm()
        
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')
    

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)  # Use custom form
            if form.is_valid():
                form.save()
                return redirect('accounts:login')
        form = CustomUserCreationForm()  # Use custom form here too
        context = {
            'form': form
        }
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')