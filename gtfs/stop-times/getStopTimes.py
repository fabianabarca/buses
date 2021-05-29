import numpy as np
import csv
import pandas as pd
import datetime


# Crear un arreglo con la tabla de paradas
stops = []
with open('stops.csv', 'r') as stopsFile:
    f = csv.reader(stopsFile)
    stopsHeader = next(f)
    for stop in f:
        stops.append(stop)


def getStopTimes():
    stop_times = []
    with open('trips.csv', 'r') as tripsFile:
        trips = csv.reader(tripsFile)
        header = next(trips)
        for trip in trips:
            stop_sequence = 0
            [route_id, service_id, trip_id, trip_headsign, trip_short_name, direction_id, shape_id, wheelchair_accessible, bikes_allowed] = trip

            startTime = getStartTime(trip_id)
            arrival_time_obj = startTime
            departure_time_obj = arrival_time_obj
            timepoint = 1
            pickup_type = '0'
            stop_headsign = ''
            drop_off_type = '0'
            shape_dist_traveled = ''
            route = getRoute(shape_id)
            # print(route)
            for terminal in route:

                with open('stops.csv', 'r') as stopsFile:
                    f = csv.reader(stopsFile)
                    stopsHeader = next(f)
                    for stop in f:
                        [stop_id, stop_code, stop_name, stop_desc, stop_lat, stop_lon, zone_id, stop_url, location_type, parent_station, stop_timezone, wheelchair_boarding] = stop
                        split = stop_id.split('_')
                        
                        if(stop_id == 'SG_0_00' or stop_id == 'SI_0_00'):
                            timepoint = 1
                        
                        if (split[0] == terminal and split[1] == direction_id):
                            # crear stop time:

                            arrival_time = arrival_time_obj.time()

                            departure_time = departure_time_obj.time()
                            stop_time = [trip_id,arrival_time,departure_time,stop_id,stop_sequence,stop_headsign,pickup_type,drop_off_type,shape_dist_traveled,timepoint]
                            stop_times.append(stop_time)
                            timeBetweenStops = getTimeBetweenStops(shape_id,stop_id)
                            arrival_time_obj = (arrival_time_obj + timeBetweenStops)
                            departure_time_obj = arrival_time_obj
                            stop_sequence = stop_sequence + 1
                            
                            if((split[0] == 'LM' and split[1] == 0) or (split[0] == 'SL' and split[1] == 0) or (split[0] == 'TU' and split[1] == 0)):
                                timepoint = 1
                            else:
                                timepoint = 0


    return stop_times






def getTimeBetweenStops(shape_id,stop_id):
    # TODO: Hacer esta funcion que recorra stops identificando cuales pertenecen a la ruta para contar las paradas
    split = stop_id.split('_')
    if (split[0] == 'LM' and split[1] == '0'):
        tripTotalTime = 15
        stopsCount = 8
    else:
        if (shape_id == 'desde_sangabriel'):
            tripTotalTime = 75
            stopsCount = 18+49-1
        if (shape_id == 'hacia_sangabriel'):
            tripTotalTime = 75
            stopsCount = 47+17-1
        if (shape_id == 'desde_acosta'):
            tripTotalTime = 75
            stopsCount = 49+12+17-1
        if (shape_id == 'hacia_acosta'):
            tripTotalTime = 75
            stopsCount = 47+12+16-1
        if (shape_id == 'desde_turrujal'):
            tripTotalTime = 90
            stopsCount = 49+12+17+9-1
        if (shape_id == 'hacia_turrujal'):
            tripTotalTime = 90
            stopsCount = 47+12+16+9-1
        if (shape_id == 'desde_sanluis'):
            tripTotalTime = 90
            stopsCount = 49+12+17+6-1
        if (shape_id == 'hacia_sanluis'):
            tripTotalTime = 90
            stopsCount = 47+12+16+6-1
    minutesBetweenStops = tripTotalTime / stopsCount
    time_obj = datetime.timedelta(hours=00, minutes=minutesBetweenStops, seconds=00)
    # print(time_obj)
    return time_obj

# Obtener la hora del viaje desde el trip_id
def getStartTime(trip_id):
    split = trip_id.split('_')
    time = split[3]
    time_obj = datetime.datetime.strptime(time, '%H:%M:%S')

    if (split[0] == 'desde' and split[1] == 'sangabriel'):
        offset = datetime.timedelta(hours=00, minutes=15, seconds=00)
        time_obj = time_obj - offset
    if (split[0] == 'desde' and split[1] == 'sanluis'):
        offset = datetime.timedelta(hours=00, minutes=15, seconds=00)
        time_obj = time_obj - offset
    if (split[0] == 'desde' and split[1] == 'turrujal'):
        offset = datetime.timedelta(hours=00, minutes=15, seconds=00)
        time_obj = time_obj - offset

    return time_obj

# Obtener la ruta (trayectoria) desde el trip_id
def getRoute(shape_id):
    # TODO: hacer esto automaticamente
    route = []
    if (shape_id == 'desde_sangabriel'):
        route = ['LM', 'SG', 'SJ']
    if (shape_id == 'hacia_sangabriel'):
        route = ['SJ', 'SG', 'LM']
    if (shape_id == 'desde_acosta'):
        route = ['SI', 'JO', 'SJ']
    if (shape_id == 'hacia_acosta'):
        route = ['SJ', 'JO', 'SI']
    if (shape_id == 'desde_turrujal'):
        route = ['TU', 'SI', 'JO', 'SJ']
    if (shape_id == 'hacia_turrujal'):
        route = ['SJ', 'JO', 'SI', 'TU']
    if (shape_id == 'desde_sanluis'):
        route = ['SL', 'SI', 'JO', 'SJ']
    if (shape_id == 'hacia_sanluis'):
        route = ['SJ', 'JO', 'SI', 'SL']
    return route

# Crear nuevo CSV con los stop_times
stop_times = getStopTimes()
with open("stop_times.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(stop_times)
