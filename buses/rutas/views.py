from django.shortcuts import get_object_or_404, render
from .models import Route, Trip, Stop, StopTime
from datetime import datetime # For current time

""" Function to execute when user goes to /rutas """
def rutas(request):
    # Get current time to pass it to nextBuses()
    now = datetime.now()

    # Get all the the routes
    routes = Route.objects.all()

    # Store all the trips
    trips = []

    # Fill trips with all the trips for all the routes
    for route in routes:
        trips.append(Trip.objects.filter(route=route))

    stop_times_SG = [] # Stop times from San Gabriel to SJ
    stop_times_Aco = [] # Stop times from Acosta to SJ
    stop_times_SJ_SG = [] # Stop times from SJ to San Gabriel
    stop_times_SJ_Aco = [] # Stop times from SJ to Acosta

    # Fill each stop_times list with its data
    for item in trips:
        for trip in item:
            if trip.trip_id == "trip1" :
                stop_times_SG.append(StopTime.objects.filter(trip=trip))
            elif trip.trip_id == "trip2":
                stop_times_Aco.append(StopTime.objects.filter(trip=trip))
            elif trip.trip_id == "trip3":
                stop_times_SJ_SG.append(StopTime.objects.filter(trip=trip))
            elif trip.trip_id == "trip4":
                stop_times_SJ_Aco.append(StopTime.objects.filter(trip=trip))

    next_bus_list_SG = []
    next_bus_list_Aco = []
    next_bus_list_SJ_SG = []
    next_bus_list_SJ_Aco = []

    # Fill the next 3 buses from SG to SJ
    for stop_times in stop_times_SG:
        next_bus_list_SG = (nextBuses(stop_times, now))
    
    # Fill the next 3 buses from Acosta to SJ
    for stop_times in stop_times_Aco:
        next_bus_list_Aco = (nextBuses(stop_times, now))

    # Fill the next 3 buses from SJ to SG
    for stop_times in stop_times_SJ_SG:
        next_bus_list_SJ_SG = (nextBuses(stop_times, now))

    # Fill the next 3 buses from SJ to Acosta
    for stop_times in stop_times_SJ_Aco:
        next_bus_list_SJ_Aco = (nextBuses(stop_times, now))

    context = {
        'routes': routes, # List of routes
        'next_bus_list_SG': next_bus_list_SG, # Next 3 buses from SG to SJ
        'next_bus_list_Aco': next_bus_list_Aco, # Next 3 buses from Acosta to SJ
        'next_bus_list_SJ_SG': next_bus_list_SJ_SG, # Next 3 buses from SJ to SG
        'next_bus_list_SJ_Aco': next_bus_list_SJ_Aco, # Next 3 buses SJ to Acosta
        
    }

    return render(request, 'rutas.html', context)

""" Function to execute when user goes to specific Route (E.g. /rutas/sangabriel o /rutas/acosta) """
def ruta(request, url_ruta):
    # Get the route depending on the url
    route = get_object_or_404(Route, url=url_ruta)

    # Get the stop object that is the "Terminal" in San Gabriel
    stop = get_object_or_404(Stop, stop_id="terminal") # Al asignar los IDs cambiar por el ID a usar para la terminal

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

    # Get all the the stops to send theit Coordinates
    # in order to fill the map
    stops = Stop.objects.all()

    terminal_coordinates = []
    terminal_coordinates.append(stops[0].stop_lat)
    terminal_coordinates.append(stops[0].stop_lon)

    SJ_coordinates = []
    SJ_coordinates.append(stops[1].stop_lat)
    SJ_coordinates.append(stops[1].stop_lon)

    context = {
        'route': route, # Route object
        'stop': stop, # Route stop object ("terminal")
        'stop_times_list': stop_times_list, # Route stop time list (to SJ and from SJ)
        'stop_times_SJ_last': stop_times_SJ.last(), # To send the last departure from "San José" in the cases that the last row of the schedule have only a stop time for "San José"
        'bus_listRoute': bus_listRoute, # Next 3 buses from the Route to SJ
        'bus_listSJ': bus_listSJ, # Next 3 buses from SJ to the Route
        'terminal_coordinates': terminal_coordinates,
        'SJ_coordinates': SJ_coordinates,
    }

    return render(request, 'ruta.html', context)

""" Function that calculates the next 3 buses based on the current time and return them in a list (list of datetimes) """
def nextBuses(stop_times, current_time):
    bus_list = [] # List to return with the next buses

    stop_times_list = list(stop_times) # Convert the scehule given to a list
    iterator = iter(stop_times_list) # Get an iterator for the stop_times_list
    next(iterator)  # Get the first element in the list (to get next elements in the for cycle)
    for item in stop_times_list:
        if current_time.hour == item.departure_time.hour:
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
