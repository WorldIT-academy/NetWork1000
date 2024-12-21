from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login


def render_registration(request):
    error = ""
    if request.method == "POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        confirm_password= request.POST.get("confirm_password")
        if password == confirm_password:
            try: 
                User.objects.create_user(username=username, password=password)
                return redirect("login")
            except IntegrityError:
                error = "This user already exists"
        else:
            error = "Passwords don't match"   
    return render(request, "user_app/registration.html", context= {"error": error} )


def render_login(request):
    error = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password = password)
        if user != None:
            login(request, user)
            return redirect('welcome')
        else:
            error = "Username or password is not correct"
    return render(request, "user_app/login.html", context = {"error": error})

def render_welcome(request):
    return render(request,'user_app/welcome.html')