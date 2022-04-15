# Create your views here.
from django.shortcuts import render, redirect
from .models import User as User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LogInForm

# Create your views here.
def home(request):
    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    error = False
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'signin.html', {'form': form, 'error': error})

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')