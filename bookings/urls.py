from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'location/<int:location_id>/',
        views.theatres,
        name='theatres'
    ),
    path(
    'theatre/<int:theatre_id>/',
    views.shows,
    name='shows'
    ),
    path(
    'show/<int:show_id>/',
    views.seats,
    name='seats'
    ),
    path(
    'seat/<int:seat_id>/',
    views.select_seat,
    name='select_seat'
    ),
    path(
    "my-tickets/",
    views.my_tickets,
    name="my_tickets"
    ),

]