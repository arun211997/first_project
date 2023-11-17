from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request,"home.html")

def signup_page(request):
    return render(request,"signup_page.html")

def login_page(request):
    return render(request,"login_page.html")

def admin_home(request):
    return render(request,"admin_home.html")

def user_home(request):
    return render(request,"user_home.html")

# signup
def create_user(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        username=request.POST["username"]
        password=request.POST["password"]
        cpassword=request.POST["cpassword"]

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"this username is already taken,try another")
                return redirect("signup_page")
            
            elif  User.objects.filter(email=email).exists():
                messages.info(request,"this email is already exist,try another")
                return redirect("signup_page")
            else:
                user=User.objects.create_user(first_name=first_name,
                                              last_name=last_name,
                                              username=username,
                                              email=email,
                                              password=password)
                user.save()
                return redirect("login_page")
        else:
            return redirect("signup_page")
        
    else:
        return redirect("signup_page")
    
def login_funtion(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=auth.authenticate(username=username,password=password)

        if user is not None:

            # if user is exist
            auth.login(request,user)
            if(user.is_superuser):
                return redirect("admin_home")
            else:
                request.session['uid']=user.id
                return redirect("user_home")
        else:
            messages.info(request,"invalid username and password")
            return redirect("login_page")
    else:
        return redirect("login_page")
    
def logout(request):
	auth.logout(request)
	return redirect('home')


# python manage.py createsuperuser  -admin



            



