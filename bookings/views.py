from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Location, Theatre, Show, Seat, Booking
from .forms import BookingForm

# Create your views here.
def index(request):
    locations = Location.objects.all()
    context = {'locations' : locations}
    return render(request, 'bookings/index.html',context)
def theatres(request, location_id):
    location = Location.objects.get(id=location_id)

    theatres = Theatre.objects.filter(
        location=location
    )

    context = {
        'location': location,
        'theatres': theatres,
    }

    return render(
        request,
        'bookings/theatres.html',
        context
    )
def shows(request, theatre_id):
    theatre = Theatre.objects.get(id=theatre_id)

    shows = Show.objects.filter(
        theatre=theatre
    )

    context = {
        'theatre': theatre,
        'shows': shows,
    }

    return render(
        request,
        'bookings/shows.html',
        context
    )
def shows(request, theatre_id):
    theatre = Theatre.objects.get(id=theatre_id)

    shows = Show.objects.filter(
        theatre=theatre
    )

    context = {
        'theatre': theatre,
        'shows': shows,
    }

    return render(
        request,
        'bookings/shows.html',
        context
    )
def seats(request, show_id):
    show = Show.objects.get(id=show_id)

    seats = Seat.objects.filter(
        show=show
    )

    context = {
        'show': show,
        'seats': seats,
    }

    return render(
        request,
        'bookings/seats.html',
        context
    )
@login_required
def select_seat(request, seat_id):
    seat = Seat.objects.get(id=seat_id)

    if request.method == "POST":

        # Get the latest seat data from the database
        seat.refresh_from_db()

        # Check if another user already booked it
        if seat.is_booked:
            return render(
                request,
                "bookings/already_booked.html",
                {
                    "seat": seat,
                }
            )

        # Create booking
        booking = Booking.objects.create(
            user=request.user
        )

        # Update seat
        seat.booking = booking
        seat.is_booked = True
        seat.save()

        return redirect(
            "seats",
            show_id=seat.show.id
        )

    context = {
        "seat": seat,
    }

    return render(
        request,
        "bookings/select_seat.html",
        context
    )
@login_required
def my_tickets(request):

    seats = Seat.objects.filter(
        booking__user=request.user
    )

    context = {
        "seats": seats,
    }

    return render(
        request,
        "bookings/my_tickets.html",
        context
    )