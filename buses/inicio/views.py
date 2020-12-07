from django.shortcuts import get_object_or_404, render
from rutas.models import Route, Trip, Stop, StopTime
from datetime import datetime # For current time

# Create your views here.

def index(request):
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

    # print(next_bus_list_SG)
    
    # Fill the next 3 buses from Acosta to SJ
    for stop_times in stop_times_Aco:
        next_bus_list_Aco = (nextBuses(stop_times, now))

    # print(next_bus_list_Aco)

    # Fill the next 3 buses from SJ to SG
    for stop_times in stop_times_SJ_SG:
        next_bus_list_SJ_SG = (nextBuses(stop_times, now))

    # print(next_bus_list_SJ_SG)

    # Fill the next 3 buses from SJ to Acosta
    for stop_times in stop_times_SJ_Aco:
        next_bus_list_SJ_Aco = (nextBuses(stop_times, now))

    # print(next_bus_list_SJ_Aco)

    # Fecha

    ahora = datetime.now()
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    dia = dias[ahora.weekday()]
    fecha = ahora.day
    mes = meses[ahora.month - 1]
    ano = ahora.year

    context = {
        'routes': routes, # List of routes
        'next_bus_list_SG': next_bus_list_SG, # Next 3 buses from SG to SJ
        'next_bus_list_Aco': next_bus_list_Aco, # Next 3 buses from Acosta to SJ
        'next_bus_list_SJ_SG': next_bus_list_SJ_SG, # Next 3 buses from SJ to SG
        'next_bus_list_SJ_Aco': next_bus_list_SJ_Aco, # Next 3 buses SJ to Acosta
        'dia': dia,
        'fecha': fecha,
        'mes': mes,
        'ano': ano,
    }

    return render(request, 'index.html', context)

def acerca(request):
    return render(request, 'acerca.html')

    """ Function that calculates the next 3 buses based on the current time and return them in a list (list of datetimes) """
def nextBuses(stop_times, current_time):
    bus_list = [] # List to return with the next buses

    stop_times_list = list(stop_times) # Convert the scehdule given to a list
    iterator = iter(stop_times_list) # Get an iterator for the stop_times_list
    next(iterator)  # Get the first element in the list (to get next elements in the for cycle)

    for item in stop_times_list:
        # Change from datetime to string
        # This is for displaying the times in AM/PM format
        time1_string = item.departure_time.strftime("%-I:%M %p")

        if current_time.hour == item.departure_time.hour:
            if current_time.minute < item.departure_time.minute:
                bus_list = []
                bus_list.append(time1_string)
                try:
                    # Change from datetime to string for the next 2 buses
                    # This is for displaying the times in AM/PM format
                    time2_string = next(iterator).departure_time.strftime("%-I:%M %p")
                    bus_list.append(time2_string)

                    time3_string = next(iterator).departure_time.strftime("%-I:%M %p")
                    bus_list.append(time3_string)
                except:
                    break
                return bus_list

        elif current_time.hour <= item.departure_time.hour:
            bus_list = []
            bus_list.append(time1_string)
            try:
                # Change from datetime to string for the next 2 buses
                # This is for displaying the times in AM/PM format
                time2_string = next(iterator).departure_time.strftime("%-I:%M %p")
                bus_list.append(time2_string)

                time3_string = next(iterator).departure_time.strftime("%-I:%M %p")
                bus_list.append(time3_string)
            except:
                break
            return bus_list
        
        else:
            bus_list.append(time1_string)
        try:
            next(iterator)
        except:
            break
    
    return bus_list