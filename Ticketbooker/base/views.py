from django.shortcuts import render
# from django.db.models import Count
from django.db.models import Sum
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import StageEventShow, TicketBooking
from .forms import TicketBookingForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def book_ticket(request):
    context = {}
    if request.method == "POST":
        ...

  
    data = (    StageEventShow.objects
                                .annotate(total_seats=Sum('ticketbooking__no_of_seats'))  # Sum of no_of_seats
                                .values('id', 'start_time', 'end_time', 'total_seats', 'stage_event_id') 
    )
    print(data)
    context['result'] = data
    

    return render(request, "base/bindex.html", context)
# views.py


def book(request, id):
    stage_event_show = get_object_or_404(StageEventShow, id=id)

    if request.method == 'POST':
        form = TicketBookingForm(request.POST)
        if form.is_valid():
            ticket_booking = form.save(commit=False)  # Don't save to DB yet
            ticket_booking.stage_event_show = stage_event_show  # Set the foreign key
            ticket_booking.save()  # Now save to DB
            return redirect('book-ticket')  # Redirect to a success page or another appropriate page
    else:
        form = TicketBookingForm()

    return render(request, 'base/booking_form.html', {
        'form': form,
        'stage_event_show': stage_event_show,
    })
