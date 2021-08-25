from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def login(request):
    if request.method =='POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            #id를 id에 password를 password로 받아라
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            #있으면 로그인 해라
            if user is not None:
                #요청에 따른 user
                login(request,user)
        #if문 세개 다 거친다.
        return redirect("home")
    else:
        form=AuthenticationForm()
        return render(request,'login.html',{'form':form})

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