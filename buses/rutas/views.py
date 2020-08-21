from django.shortcuts import get_object_or_404, render
from .models import Route, Trip, Stop, StopTime
from datetime import datetime # For current time

def rutas(request):
    return render(request, 'rutas.html')

def ruta(request, url_ruta):
    # Get the route depending on the url
    route = get_object_or_404(Route, url=url_ruta)

    # Get the stop object that is the "Terminal" in San Gabriel
    stop = get_object_or_404(Stop, stop_id="terminal")

    # Get the trip for this route
    trip = Trip.objects.filter(route=route)

    # Get the Stop Times for this trip
    # In this version there are only DEPARTURE TIMES FROM THE "TERMINAL" AND FROM SAN JOSE
    stop_times_Route = StopTime.objects.filter(trip=trip[0]) # Stop times for this Route departures ("San Gabriel" or "Acosta")
    stop_times_SJ = StopTime.objects.filter(trip=trip[1]) # Stop times for "San José" departures

    stop_times_list = zip(stop_times_Route, stop_times_SJ) # Make a list of tuples in order to display the two stop times in the schedule row

    # Get current time to display it in the template
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    context = {
        'route': route,
        'current_time': current_time,
        'stop': stop,
        'stop_times_list': stop_times_list,
        'stop_times_SJ_last': stop_times_SJ.last(), # To send the last departure from "San José" in the cases that the last row of the schedule have only a stop time for "San José"
    }

    return render(request, 'ruta.html', context)