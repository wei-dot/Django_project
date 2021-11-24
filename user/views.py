from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="Login")
def index(request):
    return render(request, 'user/index.html')

def sign_in(request):
    form = forms.LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  #重新導向到首頁
    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context)

def log_out(request):
    logout(request)
    return redirect('login')

def sign_up(request):
    form = forms.RegisterForm()

    if request.method == "POST":
        form =  forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  #重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)

