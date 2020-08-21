from django.shortcuts import get_object_or_404, render
from .models import Route, Trip, Stop, StopTime
from datetime import datetime # For current time

def rutas(request):
    return render(request, 'rutas.html')

def ruta(request, url_ruta):
    route = get_object_or_404(Route, url=url_ruta)

    stop = get_object_or_404(Stop, stop_id="terminal")

    trip = Trip.objects.filter(route=route)

    stop_times = StopTime.objects.filter(trip=trip[0])

    # Get current time to display it in the template
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    context = {
        'route': route,
        'current_time': current_time,
        'stop': stop,
        'stop_times': stop_times,
    }

    return render(request, 'ruta.html', context)