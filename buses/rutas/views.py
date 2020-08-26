from django.shortcuts import get_object_or_404, render
from .models import Route, Trip, Stop, StopTime
from datetime import datetime # For current time

""" Function to execute when user goes to /rutas """
def rutas(request):
    # Get current time to display it in the template
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Get the route depending on the url
    # routes = Route.objects.all()

    # Get the stop object that is the "Terminal" in San Gabriel
    # stop = get_object_or_404(Stop, stop_id="terminal")

    # Get the trip for this route
    trips = []

    # for route in routes:
    #     trips.append(Trip.objects.filter(route=route))

    # print(trips)

    # Get the Stop Times for this trip
    # In this version there are only DEPARTURE TIMES FROM THE "TERMINAL" AND FROM SAN JOSE
    # stop_times_Route = StopTime.objects.filter(trip=trips[0]) # Stop times for this Route departures ("San Gabriel" or "Acosta")
    # stop_times_SJ = StopTime.objects.filter(trip=trips[1]) # Stop times for "San José" departures

    # print(stop_times_Route)

    # stop_times_list = zip(stop_times_Route, stop_times_SJ) # Make a list of tuples in order to display the two stop times in the schedule row
    
    # Get the next 3 buses list from the Route to San Jose
    # bus_listRoute = nextBuses(stop_times_Route, now)
    # Get the next 3 buses list from San Jose to the Route
    # bus_listSJ = nextBuses(stop_times_SJ, now)

    context = {
        'current_time': current_time,
        # 'bus_listRoute': bus_listRoute, # Next 3 buses
        # 'bus_listSJ': bus_listSJ, # Next 3 buses
    }

    return render(request, 'rutas.html', context)

""" Function to execute when user goes to specific Route (E.g. /rutas/sangabriel o /rutas/acosta) """
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
    
    # Get the next 3 buses list from the Route to San Jose
    bus_listRoute = nextBuses(stop_times_Route, now)
    # Get the next 3 buses list from San Jose to the Route
    bus_listSJ = nextBuses(stop_times_SJ, now)

    context = {
        'route': route,
        'current_time': current_time,
        'stop': stop,
        'stop_times_list': stop_times_list,
        'stop_times_SJ_last': stop_times_SJ.last(), # To send the last departure from "San José" in the cases that the last row of the schedule have only a stop time for "San José"
        'bus_listRoute': bus_listRoute, # Next 3 buses
        'bus_listSJ': bus_listSJ, # Next 3 buses
    }

    return render(request, 'ruta.html', context)

""" Function that calculates the next 3 buses and return them in a list (list of datetimes) """
def nextBuses(stop_times, current_time):
    bus_list = [] # List to return with the next buses

    stop_times_list = list(stop_times) # Convert the scehule given to a list
    iterator = iter(stop_times_list) # Get an iterator for the stop_times_list
    next(iterator)  # Get the first element in the list (to get next elements in the for cycle)
    for item in stop_times_list:
        if current_time.hour == item.departure_time.hour:
            print(current_time.minute)
            if current_time.minute < item.departure_time.minute:
                try:
                    bus_list = []
                    bus_list.append(item.departure_time)
                    bus_list.append(next(iterator).departure_time)
                    bus_list.append(next(iterator).departure_time)
                    return bus_list
                except:
                    break
            else:
                try:
                    # next(iterator)
                    bus_list = []
                    bus_list.append(next(iterator).departure_time)
                    bus_list.append(next(iterator).departure_time)
                    bus_list.append(next(iterator).departure_time)
                    return bus_list
                except:
                    break
        elif current_time.hour + 1 == item.departure_time.hour:
            try:
                bus_list = []
                bus_list.append(item.departure_time)
                bus_list.append(next(iterator).departure_time)
                bus_list.append(next(iterator).departure_time)
                return bus_list
            except:
                break
        else:
            bus_list.append(item.departure_time)
        try:
            next(iterator)
        except:
            break
    return bus_list
