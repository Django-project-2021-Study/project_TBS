from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['userid']
        password=request.POST['userpw']
        user=auth.authenticate(request, username=username,password=password)
        if user is not None:
           auth.login(request, user)
           return redirect('home')
        else:
            return render(request,'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'login.html')


def signup(request):
    if request.method == "POST":
        if request.POST["userpw"]== request.POST["userrepw"]:
            user=User.objects.create_user(username=request.POST["userid"],password=request.POST["userpw"])

            auth.login(request,user)
            return redirect('home')
        return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect("home")