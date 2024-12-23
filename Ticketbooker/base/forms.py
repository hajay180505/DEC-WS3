# forms.py
from django import forms
from .models import TicketBooking

class TicketBookingForm(forms.ModelForm):
    class Meta:
        model = TicketBooking
        fields = ['customer', 'no_of_seats', 'price']  # Exclude stage_event_show as it will be set in the view
