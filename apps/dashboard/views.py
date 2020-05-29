from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Course

# Create your views here.


def dashboard(request):
    allcourses = Course.objects.all()
    return render(request, "user/dashboard.html", {'allcourses':allcourses})

def newcourse(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['image']
        description = request.POST['description']
        price = request.POST['price']

        course = Course(title=title, image=image, description=description, price=price)
        course.save()
        messages.info(request, 'New course succesfully added')
        return redirect('dashboard')

    else:
        return render(request, "user/newcourse.html")


