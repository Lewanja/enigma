from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect
from .forms import BookingForm


def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_success', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'schedule_visit/create_booking.html', {'form': form})


