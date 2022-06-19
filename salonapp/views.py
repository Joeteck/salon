import re
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import mysql.connector




# LOGIN_URL = 'login'
# # Create your views here.
# @login_required
def home(request):
    salon = Salon.objects.all()
    return render(request, 'home.html', {'salons':salon} )

def preload(request):
    return render(request, 'preload.html')
def location(request):
    return render(request, 'location.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        birthdate = request.POST['birthdate']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exist Please try another One.')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Please Username has been used try using another One.')
                return redirect('register')
            else:
                user= User.objects.create(username=username, email=email, password=make_password(password), contact=contact, birthdate=birthdate)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same. Try again...')
            return redirect('register')
    else:    
        return render(request, 'register.html' )

# in django_blogs/settings.py

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        p = request.POST['password']
        password = make_password(p)
        
        if  username==username and password==password:
            auth.login(request, User)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is not correct... Please try again')
        return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('/')

def service(request):
    
    service = Service.objects.all()
    # if request.method == 'POST':
    #     date = request.POST['time']
    #     numberofpeople = request.POST['numberofpeople']
    #     price = Service.objects.get(request.id)
    #     amount = numberofpeople*price.price

    #     booking = Booking.objects.create(date=date, numberofpeople=numberofpeople, amount=amount)
    # if len(service)>0:
    #     data = Service.objects.get(salonid=Salon)
    #     context = {"data":data}
    return render(request, 'service.html', {'service':service} )

    # context = {'form':form}
    # if request.method == 'POST':

    #         amount=
    #         form.save()
    #         messages.success(request, 'Your booking has been placed... Just a moment for the Stylist to Approve it.')
    #         return redirect('home')
    #     else:
    #         messages.info(request, 'There is an issue with one of the fields please make sure you correctly fill the fields')
    #         return redirect('newservice')
    # else:
    #     return render(request, 'service.html', context)

def bookings(request):
    context = {}
    bookings = Booking.objects.filter(userid=request.user.id)
    if len(bookings)>0:
        data = Booking.objects.get(userid=request.user.id)
        context["data"] = data
    return render(request, 'bookings.html', context)

def search(request):
    context = {}
    bookings = Salon.objects.filter()
    if len(bookings)>0:
        data = Booking.objects.get(userid=request.user.id)
        context["data"] = data
    return render(request, 'search.html', context)

def profile(request):
    # profile = User.objects.get(username=username){'profile' : profile}
    # if request.methods == 'POST':
    #     pass
    # else:
    #     pass
    return render(request, 'profile.html')

def rate(request):
    if request.method == 'POST':
        pass
    else:
        pass
        return render(request, 'rate.html')

def salon(request):
    current_user = User.objects.get()
    print(current_user)
    # x = Salon.objects.filter(id__exact=current_user).update()
    form = AddSalonForm()
    if request.method == "POST":
        form = AddSalonForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'You''ve Added your Salon... You can now add your Services.')
                return redirect('newservice')
            except:
                # pass
        # else:
                messages.info(request, 'There is an issue with one of the fields please make sure you correctly fill the fields')
                return redirect('salon')
    else:
        return render(request, 'salon.html', {'form':form})
    # if request.method == 'POST':
    #     salonname =request.POST['salonname']
    #     address =request.POST['address']
    #     starttime =request.POST['starttime']
    #     closetime =request.POST['closetime']
    #     image =request.POST['image']

    #     form= Salon.objects.create(salonname=salonname, address=address, starttime=starttime, closetime=closetime, image=image )
    #     form.save()
    #     messages.success(request, 'Your Salon has been created... you can now Add your Service in your dashboard')
    #     return redirect('salondashboard')
    #     # else:
    #     #     messages.info(request, 'There is an issue with one of the fields please make sure you correctly fill the fields')
    #     #     return redirect('salon')
    # else:    
    #     return render(request, 'salon.html')

def newservice(request):
    form = AddServiceForm()
    if request.method == "POST":
        form = AddServiceForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'You''ve Added Service to your Salon.')
                return redirect('salondashboard')
            except:
                pass
        else:
            messages.info(request, 'There is an issue with one of the fields please make sure you correctly fill the fields')
            return redirect('newservice')
    else:
        return render(request, 'newservice.html', {'form':form})

def salondashboard(request):
    return render(request, 'salondashboard.html')

def salonprofile(request):
    return render(request, 'salonprofile.html')

def salonbookings(request):
    bookings = Booking.objects.filter(salonid=request.salon.id).order_by('-date')
    data = Booking.objects.get(salonid=request.salon.id)

    if request.method =="POST":
        id = request.POST.getlist('check')
        bookings.update(approved=False)
        
        for x in id:
            Booking.objects.filter(pk=int(x)).update(approved=True)
    else:
        context = {}
        if len(bookings)>0:
            context["data"] = data
        return render(request, 'salonbookings.html')