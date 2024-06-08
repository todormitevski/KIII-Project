from django.shortcuts import render, redirect

from event_app.forms import EventForm
from event_app.models import *


# Create your views here.


def index(request):
    events = Event.objects.filter(user=request.user).all()
    return render(request, 'index.html', {'events': events})


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, files=request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user

            bands = event.band_input.split(",")
            event.save()
            for band in bands:
                band = band.strip()
                band_obj = Band.objects.filter(name=band).first()
                if band_obj:
                    band_obj.num_events += 1
                    band_obj.save()
                    EventBand.objects.create(band=band_obj, event=event)

            return redirect('home')
    else:
        form = EventForm()

    return render(request, 'add_event.html', {'form': form})


def details(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'details.html', {"event": event})


def edit_event(request, event_id):
    event_instance = Event.objects.get(id=event_id)
    if request.method == 'POST':
        event = EventForm(request.POST, request.FILES, instance=event_instance)
        if event.is_valid():
            event.save(commit=False)
            if 'poster' in request.FILES:
                event.poster = request.FILES['poster']
            event.save()
            return redirect('home')
    else:
        event = EventForm(instance=event_instance)
        return render(request, 'edit_event.html', {"form": event})


def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('home')
