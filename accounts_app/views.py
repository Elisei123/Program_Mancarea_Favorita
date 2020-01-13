from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.db.models.functions import Lower
# Create your views here.


#Check valid email
def is_email(string):
    from django.core.exceptions import ValidationError
    from django.core.validators import EmailValidator

    validator = EmailValidator()
    try:
        validator(string)
    except ValidationError:
        return False

    return True


#Check valid username
def UsernameValidator(string):
    from django.contrib.auth.validators import UnicodeUsernameValidator
    validator = UnicodeUsernameValidator()
    try:
        validator(string)
    except ValidationError:
        return False

    return True



def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST['username'].lower()
            if UsernameValidator(username):
                email = request.POST['email'].lower()

                if is_email(email):
                    password1 = request.POST['password1']
                    password2 = request.POST['password2']
                    if password1 == password2:
                        if User.objects.filter(username=username).exists():
                            messages.info(request, 'Username-ul este folosit.')
                            return redirect('register')
                        elif User.objects.filter(email=email).exists():
                            messages.info(request, 'Email-ul este folosit.')
                            return redirect('register')
                        else:
                            user = User.objects.create_user(username=username, password=password1, email=email)
                            user.save()
                            print("User created")
                            messages.success(request, 'Contul a fost creat cu succes!')
                            user = auth.authenticate(username=username, password=password1)
                            auth.login(request, user)
                            return redirect("/")
                    else:
                        messages.info(request, 'Parola de verificare nu este la fel.')
                        return redirect('register')
                else:
                    messages.info(request, 'Email-ul nu este valid ("exemplu@gmail.com")!')
                    return redirect('register')
            else:
                messages.info(request, 'Username-ul contine spatiu sau caractere interzise!')
                return redirect('register')
        else:
            return render(request, "register.html")


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            print("Logat")
            username = request.POST['username'].lower()
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Welcome back!')
                return redirect("/")
            else:
                messages.error(request, "Username-ul sau parola nu sunt valide!")
                return redirect('login')

        else:
            return render(request, "login.html")

@login_required

def logout(request):
    auth.logout(request)
    return redirect('/')

def settings(request):
    if request.method == "POST":
        user_curent = request.user
        username = request.POST['username']
        email = request.POST['email']
        if user_curent.username == username:
            if user_curent.email != email:
                if User.objects.filter(email=email).exists():
                    messages.info(request, "Email-ul exista deja in baza de date.")
                    return redirect('settings')
                else:
                    user_curent.email = email
                    user_curent.save()
                    messages.info(request, "Email-ul a fost schimbat cu succes!")
                    return redirect('settings')
            else:
                messages.info(request, "Nu a fost nimic de modificat!")
                return redirect('settings')
        else:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Nickname-ul exista deja in baza de date.")
                return redirect('settings')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request, "Email-ul exista deja in baza de date.")
                    return redirect('settings')
                else:
                    user_curent.email = email
                    user_curent.username = username
                    user_curent.save()
                    messages.info(request, "Datele au fost schimbate cu succes!")
                    return redirect('settings')
    else:
        return render(request, "settings.html")