from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import Profile


def render_registration(request):
    # Змінна, що відпвідає за текст помилки. Ця змінна передається через context та відображається у шаблоні
    error = ""
    # Якщо відправляється запит з типом POST (якщо відправляється форма)
    if request.method == "POST":
        # Отримуємо дані з форми та зберігаємо у змінні
        username= request.POST.get("username")
        password= request.POST.get("password")
        confirm_password= request.POST.get("confirm_password")
        # Якщо користувач двічі ввів однаковий пароль
        if password == confirm_password:
            # Відлювлюємо помилку у разі, якщо користувач вже існує
            try: 
                # Створення користувача у БД
                User.objects.create_user(username=username, password=password)
                # Перенапрвлення на сторінку логіну
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
        # Функція authenticate повертає об'єкт користувача, якщо юзер з такими логіном та паролем існує. Інкаше повртає None
        user = authenticate(request, username= username, password = password)
        # Якщо користувач існує (користувачч ввів усі дані правильно у формі)
        if user != None:
            # Авторизуємо користувача
            login(request, user)
            # Перенаправляємо користувача на "сторінку-привітання"
            return redirect('welcome')
        else:
            error = "Username or password is not correct"
    return render(request, "user_app/login.html", context = {"error": error})

def render_welcome(request):
    # Перевіяємо, чи авторизувався користувач
    if request.user.is_authenticated:
        return render(request,'user_app/welcome.html')
    else:
        return redirect("login")
    
def logout_user(request):
    # Вихід із акаунту
    logout(request)
    return redirect('login')

def render_profiles(request):
    all_profiles = Profile.objects.all()
    return render(request, "user_app/profiles.html", context={"all_profiles": all_profiles})