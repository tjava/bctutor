from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Course, Userdetail

# Create your views here. request.user.is_authenticated

#@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated:
        id = request.session['id']
        allcourses = Course.objects.all()
        userdetail = Userdetail.objects.get(user_id=id)
        return render(request, "user/dashboard.html", {'allcourses':allcourses, 'userdetail':userdetail})
    else:
        return redirect('login')


def becomeinstructor(request):
    allcourses = Course.objects.all()
    return render(request, "user/dashboard.html", {'allcourses':allcourses})



def allcourses(request):
    id = request.session['id']
    allcourses = Course.objects.filter(user_id=id)
    return render(request, "user/allcourses.html", {'allcourses':allcourses})


def shareprofile(request):

    id = request.session['id']
    user = User.objects.get(id=id)
    userdetail = Userdetail.objects.get(user_id=id)

    return render(request, "user/shareprofile.html", {'user':user,'userdetail':userdetail,})



def editprofile(request):
    id = request.session['id']

    if request.method == 'POST':
        image = request.FILES['image']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        fb_link = request.POST['fb_link']
        phone_number = request.POST['phone_number']
        specialize = request.POST['specialize']
        about = request.POST['about']
        state = request.POST['state']
        city = request.POST['city']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name

        if password:
            if len(password) < 8:
                messages.info(request, 'Password most be atleast 8 character')
                return render(request, "user/editprofile.html")
            elif password != confirm_password:
                messages.info(request, 'Password do not match')
                return render(request, "user/editprofile.html")
            else:
                user.set_password(password)
                user.save()
                messages.info(request, 'Password changed, please login again')
                return redirect('login')


        userdetail = Userdetail.objects.get(user_id=id)
        userdetail.fb_link = fb_link
        userdetail.phone_number = phone_number
        userdetail.specialize = specialize
        userdetail.about = about
        userdetail.state = state
        userdetail.city = city
        userdetail.image = image

        user.save()
        userdetail.save()
        messages.info(request, 'Save Changed')
        return redirect('dashboard')

    else:
        user = User.objects.get(id=id)
        userdetail = Userdetail.objects.get(user_id=id)

        return render(request, "user/editprofile.html", {'user':user,'userdetail':userdetail,})



def newcourse(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_id = request.session['id']
            title = request.POST['title']
            image = request.FILES['image']
            description = request.POST['description']
            price = request.POST['price']

            course = Course(user_id=user_id, title=title, image=image, description=description, price=price)
            course.save()
            messages.info(request, 'New course succesfully added')
            return redirect('allcourses')

        else:
            return render(request, "user/newcourse.html")
    else:
        return redirect('login')



def single(request):
    id = request.GET['id']

    allcourses = Course.objects.get(id=id)
    return render(request, "user/single.html", {'allcourse': allcourses})



    
def editcourse(request):
    id = request.GET['id']

    if request.method == 'POST':
        from django.utils.datastructures import MultiValueDictKeyError
        try:
            image = request.FILES['image']
        except MultiValueDictKeyError:
            image = False
        #image = request.FILES.get['image', False]
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']

        course = Course.objects.get(id=id)
        course.title = title
        course.description = description
        course.price = price

        if image:
            course.image = image

        course.save()
        messages.info(request, 'Save Changed')
        return redirect('allcourses')

    else:
        course = Course.objects.get(id=id)

        return render(request, "user/editcourse.html", {'course':course})



def search(request):
    # id = request.GET['q']

    # allcourses = Course.objects.get(id=id)
    return render(request, "user/search.html")



def deletecourse(request):
    id = request.GET['id']

    deletecourse = Course.objects.get(id=id)
    deletecourse.delete()
    messages.info(request, 'Course deleted succesfully')
    return redirect('allcourses')