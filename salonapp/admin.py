from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Salon)
admin.site.register(Service)
admin.site.register(Rating)
admin.site.register(Booking)