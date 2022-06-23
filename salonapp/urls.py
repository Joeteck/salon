from django.urls import path
from . import views

urlpatterns = [
    path('', views.preload, name='preload'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('location', views.location, name='location'),
    path('service', views.service, name='service'),
    path('bookings', views.bookings, name='bookings'),
    path('profile', views.profile, name='profile'),
    path('rate', views.rate, name='rate'),
    path('salon', views.salon, name='salon'),
    path('salondashboard', views.salondashboard, name='salondashboard'),
    path('salonprofile', views.salonprofile, name='salonprofile'),
    path('salonbookings', views.salonbookings, name='salonbookings'),
    path('newservice', views.newservice, name='newservice'),
    path('logout', views.logout, name='logout'),
    path('search', views.search, name='search'),
]