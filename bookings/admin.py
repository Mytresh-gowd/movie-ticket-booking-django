from django.contrib import admin
from .models import Location, Theatre, Show, Seat, Booking

# Register your models here.
admin.site.register(Location)
admin.site.register(Theatre)
admin.site.register(Show)
admin.site.register(Seat)
admin.site.register(Booking)



