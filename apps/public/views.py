from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from apps.dashboard.models import Course, Userdetail

#messages.info(request, 'Email already taken')

def home(request):
    return render(request, "public/home.html")



def contact(request):
    return render(request, "public/contact.html")



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['id'] = user.id
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, "public/login.html", {'email':email})

    else:
        return render(request, "public/login.html")



def logout(request):
    auth.logout(request)
    return redirect('/')



def register(request):

    if request.method == 'POST':

        Error = {}

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if first_name == "":
            Error = 'First name is required'
            messages.info(request, 'First name is required')

        if last_name == "":
            Error = 'Last name is required'
            messages.info(request, 'Last name is required')

        if email == "":
            Error = 'Email is required'
            messages.info(request, 'Email is required')

        if password == "":
            Error = 'Password name is required'
            messages.info(request, 'Password name is required')

        if len(password) < 8:
            Error = 'Password most be atleast 8 character'
            messages.info(request, 'Password most be atleast 8 character')

        if password != confirm_password:
            Error = 'Password do not match'
            messages.info(request, 'Password do not match')

        if User.objects.filter(email=email).exists():
            Error = 'Email already taken'
            messages.info(request, 'Email already taken')


        if Error:
            user = {"first_name":first_name, "last_name":last_name, "email":email}
            return render(request, "public/signup.html", {'user':user})
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=email, email=email, password=password)
            user.save()
            Userdetail.objects.create(user=user)
            return render(request, "public/login.html")

    else:
        return render(request, "public/signup.html")

