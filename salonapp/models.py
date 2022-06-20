# Create your models here.
from django.db import models
from django.urls import reverse
# Create your models here.
from datetime import date
from django.db import models
from django.utils.timezone import now



# Create your models here.
class User(models.Model):
    username = models.CharField('Username',max_length=50, blank=False, unique=True)
    password = models.CharField('Password',max_length=200, blank=False)
    email = models.EmailField('Email',unique=True)
    image = models.ImageField(upload_to='images', default='default.gif',)
    birthdate = models.DateField()
    contact = models.CharField('Phone Number', max_length=14)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Salon(models.Model):
    salonname = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'images', default='default.gif',)
    stylistid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    starttime = models.TimeField()
    closetime = models.TimeField()

    def __str__(self):
        return self.salonname

  
class Service(models.Model):
    servicename = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to = 'images', default='default.gif')
    salonid = models.ManyToManyField(Salon)

    def __str__(self):
        return self.servicename

class Rating(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    serviceid = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField()
    feedback = models.TextField(max_length=720, null=True, blank=True)

class Booking( models.Model):
    serviceid = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    numberofpeople = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    status = models.BooleanField("approved", default=False)
    date = models.TimeField()
    created_date = models.DateTimeField(default=now, editable=False)

class Favorite(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    salonid = models.ForeignKey(Salon, on_delete=models.CASCADE, null=True, blank=True)
    save = models.BooleanField()