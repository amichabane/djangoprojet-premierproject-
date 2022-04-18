# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User as User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LogInForm,EditForm

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


@login_required
def profile(request):
    user = User.objects.get(id=request.user.id)
    signup = User.objects.get(email=user)

    form = EditForm(request.POST)
    if form.is_valid():
        note = form.save(commit=False)
        note.user = request.user
        note.save()
        return redirect("profile")

    return render(request, 'profile.html', locals())

@login_required
def changePassword(request):
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'changePassword.html', locals())