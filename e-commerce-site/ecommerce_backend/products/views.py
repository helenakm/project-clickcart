from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import SignUpForm
from django import forms



#super user: Username: admin, Password: password

def home(request):
    return render(request, 'home.html', {})


def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': "Invalid username or password"})

    else:
         return render(request, 'login.html', {}) 

def logout_user(request):
       logout(request)
       messages.success(request, ("You have been logged out"))
       return redirect('home') 

def register_user(request):
    
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            if form.errors.get('username'):
                messages.error(request, "Username is already in use.")
                return redirect('register')

            if form.errors.get('email'):
                messages.error(request, "Email is already in use.")    
                return redirect('register')
            else:
                messages.error(request, "Error! Try again")    
                return redirect('register')
    else:        
        return render(request, 'register.html', {'form':form})

def reset_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'reset_password.html')

        try:
            user = User.objects.get(email=email)
            user.password = make_password(new_password)  # Hashes the new password before saving
            user.save()
            messages.success(request, "Password has been reset successfully. You can now log in with your new password.")
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "No account found with that email address.")
            return render(request, 'reset_password.html')

    return render(request, 'reset_password.html')