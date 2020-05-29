from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from apps.dashboard.models import Course


def home(request):
    return render(request, "public/home.html")

def contact(request):
    return render(request, "public/contact.html")

def single(request):
    id = request.GET['id']

    allcourses = Course.objects.get(id=id)
    return render(request, "public/single.html", {'allcourse': allcourses})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, "public/login.html")

    else:
        return render(request, "public/login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')



def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return render(request, "public/signup.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return render(request, "public/signup.html")
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                return render(request, "public/login.html")

        else:
            messages.info(request, 'Password do not match')
            return render(request, "public/signup.html")

    else:
        return render(request, "public/signup.html")

