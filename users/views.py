from django.shortcuts import render,redirect
from users.forms import RegisterForm,LoginForm
from users.backends import EmailBackend as em
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.


def home(request):
    return render(request,'users/home.html')


def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print('Successfully Created')
    else:
        form = RegisterForm()
    
    return render(request,'users/register.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname,password=pwd)
        print(user)
        if user is not None:
            if user.is_active==True:
                k=login(request,user)
                print(user,k)
                print('Successfull login')
                return redirect ('/home')
        else:
            print('Unsuccessfull login')

    else:
        form = LoginForm()    
    return render(request,'users/login.html',{'form':form})




def success(request):
    return render(request,'users/success.html',)

   
