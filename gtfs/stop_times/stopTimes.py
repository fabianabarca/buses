import datetime
import csv
import math


desde_acosta_shape = []
hacia_acosta_shape = []
desde_sanluis_shape = []
hacia_sanluis_shape = []
desde_turrujal_shape = []
hacia_turrujal_shape = []
desde_jorco_shape = []
hacia_jorco_shape = []
desde_sangabriel_shape = []
hacia_sangabriel_shape = []

desde_acosta_stops = []
hacia_acosta_stops = []
desde_sanluis_stops = []
hacia_sanluis_stops = []
desde_turrujal_stops = []
hacia_turrujal_stops = []
desde_jorco_stops = []
hacia_jorco_stops = []
desde_sangabriel_stops = []
hacia_sangabriel_stops = []



avg_bus_speed = 20 # km/h


def read_shapes():

    with open('shapes.csv', 'r') as f2:
        linked_stop = ''
        shapes_file = csv.reader(f2)
        next(shapes_file)
        for shape in shapes_file:
            [shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, shape_dist_traveled] = shape
            shape.append(linked_stop)
            if shape_id == 'desde_acosta':
                desde_acosta_shape.append(shape)
            if shape_id == 'hacia_acosta':
                hacia_acosta_shape.append(shape)
            if shape_id == 'desde_sanluis':
                desde_sanluis_shape.append(shape)
            if shape_id == 'hacia_sanluis':
                hacia_sanluis_shape.append(shape)
            if shape_id == 'desde_turrujal':
                desde_turrujal_shape.append(shape)
            if shape_id == 'hacia_turrujal':
                hacia_turrujal_shape.append(shape)
            if shape_id == 'desde_jorco':
                desde_jorco_shape.append(shape)
            if shape_id == 'hacia_jorco':
                hacia_jorco_shape.append(shape)
            if shape_id == 'desde_sangabriel':
                desde_sangabriel_shape.append(shape)
            if shape_id == 'hacia_sangabriel':
                hacia_sangabriel_shape.append(shape)



def read_stops():
    with open('stops.csv', 'r') as f1:
        stops_file = csv.reader(f1)
        next(stops_file)

        for stop in stops_file:
            [stop_id, stop_name, stop_desc, stop_lat, stop_lon, zone_id, stop_url, location_type, parent_station, wheelchair_boarding] = stop
            stop.append('')      # stop in shape
            split = stop_id.split('_')
            if split[0] == 'SJ' and split[1] == '1':
                hacia_acosta_stops.append(stop)
                hacia_jorco_stops.append(stop)
                hacia_sangabriel_stops.append(stop)
                hacia_turrujal_stops.append(stop)
                hacia_sanluis_stops.append(stop)
            if split[0] == 'SJ' and split[1] == '0':
                desde_acosta_stops.append(stop)
                desde_jorco_stops.append(stop)
                desde_sangabriel_stops.append(stop)
                desde_turrujal_stops.append(stop)
                desde_sanluis_stops.append(stop)
            if (split[0] == 'SG' or split[0] == 'LM') and split[1] == '1':
                hacia_sangabriel_stops.append(stop)
            if (split[0] == 'SG' or split[0] == 'LM') and split[1] == '0':
                desde_sangabriel_stops.append(stop)
            if split[0] == 'JO' and split[1] == '1':
                hacia_acosta_stops.append(stop)
                hacia_jorco_stops.append(stop)
                hacia_turrujal_stops.append(stop)
                hacia_sanluis_stops.append(stop)
            if split[0] == 'JO' and split[1] == '0':
                desde_acosta_stops.append(stop)
                desde_jorco_stops.append(stop)
                desde_turrujal_stops.append(stop)
                desde_sanluis_stops.append(stop)
            if split[0] == 'SI' and split[1] == '1':
                hacia_acosta_stops.append(stop)
                hacia_turrujal_stops.append(stop)
                hacia_sanluis_stops.append(stop)
            if split[0] == 'SI' and split[1] == '0':
                desde_acosta_stops.append(stop)
                desde_turrujal_stops.append(stop)
                desde_sanluis_stops.append(stop)
            if split[0] == 'TU' and split[1] == '1':
                hacia_turrujal_stops.append(stop)
            if split[0] == 'TU' and split[1] == '0':
                desde_turrujal_stops.append(stop)
            if split[0] == 'SL' and split[1] == '1':
                hacia_sanluis_stops.append(stop)
            if split[0] == 'SL' and split[1] == '0':
                desde_sanluis_stops.append(stop)

def find_stops_in_shape(shape, stops):
    dist_traveled_in_last_stop = 0.0
    flag = True
    for stop in stops:

        stop_id = stop[0]
        stop_lat = stop[3]
        stop_lon = stop[4]
        old_dist = 999.99               # muy grande
        stop_dist = 0.0                   # distancia entre esta parada y la anterior
        old_dist_traveled = 0.0           #
        stop_in_shape = 0.0
        for row in shape:
            shape_pt_lat = row[1]
            shape_pt_lon = row[2]
            shape_pt_sequence = row[3]
            new_dist = math.sqrt((abs(float(stop_lat)-float(shape_pt_lat)))**2 + abs((float(stop_lon)-float(shape_pt_lon)))**2)
            if new_dist < old_dist:
                old_dist = new_dist
                stop_in_shape = shape_pt_sequence

        for row in shape:
            shape_pt_sequence = row[3]
            # print(shape_pt_sequence)
            shape_dist_traveled = float(row[4])
            # dist_traveled_diff = shape_dist_traveled - old_dist_traveled
            # print("dist_traveled_diff = ", dist_traveled_diff)
            # print("shape dist traveled", shape_dist_traveled)
            # print("old dist traveled", old_dist_traveled)
            # old_dist_traveled = shape_dist_traveled
            # stop_dist = stop_dist + dist_traveled_diff

            if shape_pt_sequence == stop_in_shape:
                if flag:
                    stop_dist = 0
                    dist_traveled_in_last_stop = shape_dist_traveled
                    flag = False
                    stop.append(stop_dist)
                else:
                    print("_________")
                    print(shape_pt_sequence)
                    print(shape_dist_traveled)
                    print(dist_traveled_in_last_stop)
                    stop_dist = (shape_dist_traveled - dist_traveled_in_last_stop)
                    dist_traveled_in_last_stop = shape_dist_traveled
                    print(stop_dist)
                    stop.append(stop_dist)
                    stop_dist = 0


def getStopTimes(multiplier_factor):
    stop_times = []
    with open('trips.csv', 'r') as tripsFile:
        trips = csv.reader(tripsFile)
        header = next(trips)
        for trip in trips:
            stop_sequence = 0
            [route_id, service_id, trip_id, trip_headsign, trip_short_name, direction_id, shape_id,
             wheelchair_accessible, bikes_allowed] = trip

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
                        [stop_id, stop_name, stop_desc, stop_lat, stop_lon, zone_id, stop_url, location_type,
                         parent_station, wheelchair_boarding] = stop
                        split = stop_id.split('_')
                        if (stop_id == 'SG_0_00'):
                            timepoint = 1
                        if (split[0] == terminal and split[1] == direction_id):
                            # crear stop time:
                            if stop_id == 'SG_0_00':
                                split_time = trip_id.split('_')
                                time_sangabriel_stop = split_time[3]
                                arrival_time_obj = datetime.datetime.strptime(time_sangabriel_stop, '%H:%M:%S')
                            if stop_id == 'SI_0_00':
                                split_time = trip_id.split('_')
                                time_sanignacio_stop = split_time[3]
                                arrival_time_obj = datetime.datetime.strptime(time_sanignacio_stop, '%H:%M:%S')

                            arrival_time = (arrival_time_obj).time()
                            arrival_time = arrival_time.strftime("%H:%M:%S")
                            departure_time = arrival_time
                            stop_time = [trip_id,arrival_time,departure_time,stop_id,stop_sequence,stop_headsign,pickup_type,drop_off_type,shape_dist_traveled,timepoint]
                            #print(stop_time)
                            stop_times.append(stop_time)
                            timeSinceLastStop = getArrivalTime(shape_id, stop_id)
                            #print(timeSinceLastStop)
                            #if timepoint == 1: timeSinceLastStop = datetime.timedelta(minutes=1)

                            arrival_time_obj = (arrival_time_obj + timeSinceLastStop)

                            departure_time_obj = arrival_time_obj
                            stop_sequence = stop_sequence + 1
                            if (split[0] == 'LM' and split[1] == 0):
                                timepoint = 1
                            else:
                                timepoint = 0

    return stop_times


def getArrivalTime(shape_id, stop_id):
    #print("shape id: ", shape_id)
    #print("stop_id: ", stop_id)
    split = stop_id.split('_')
    if split[2] == '00': return datetime.timedelta(minutes=1)
    if shape_id == 'desde_sangabriel':
        for stop in desde_sangabriel_stops:
            if stop_id == stop[0]:
                distTraveled = stop[11]
                #print("dist: ", distTraveled)
                timeTraveledSinceLastStop = abs(float(distTraveled)/avg_bus_speed)
                time_diff = datetime.timedelta(hours=timeTraveledSinceLastStop)
                return time_diff
    elif shape_id == 'hacia_sangabriel':
        for stop in hacia_sangabriel_stops:
            if stop_id == stop[0]:
                distTraveled = stop[11]
                print("dist: ", distTraveled)
                timeTraveledSinceLastStop = abs(float(distTraveled)/avg_bus_speed)
                time_diff = datetime.timedelta(hours=timeTraveledSinceLastStop)
                return time_diff
    elif shape_id == 'desde_acosta':
        for stop in desde_acosta_stops:
            if stop_id == stop[0]:
                distTraveled = stop[11]
                print("dist: ", distTraveled)
                timeTraveledSinceLastStop = abs(float(distTraveled)/avg_bus_speed)
                time_diff = datetime.timedelta(hours=timeTraveledSinceLastStop)
                return time_diff
    elif shape_id == 'hacia_acosta':
        for stop in hacia_acosta_stops:
            if stop_id == stop[0]:
                distTraveled = stop[11]
                print("dist: ", distTraveled)
                timeTraveledSinceLastStop = abs(float(distTraveled)/avg_bus_speed)
                time_diff = datetime.timedelta(hours=timeTraveledSinceLastStop)
                return time_diff
    elif shape_id == 'desde_turrujal':
        for stop in desde_turrujal_stops:
            if stop_id == stop[0]:
                distTraveled = stop[11]
                print("dist: ", distTraveled)
                timeTraveledSinceLastStop = abs(float(distTraveled)/avg_bus_speed)
                time_diff = datetime.timedelta(hours=timeTraveledSinceLastStop)
                return time_diff
    elif shape_id == 'hacia_turrujal':
        for stop in hacia_turrujal_stops:
            if stop_id == stop[0]:
                distTraveled = stop[11]
                print("dist: ", distTraveled)
                timeTraveledSinceLastStop = abs(float(distTraveled)/avg_bus_speed)
                time_diff = datetime.timedelta(hours=timeTraveledSinceLastStop)
                return time_diff
    elif shape_id == 'desde_sanluis':
        for stop in desde_sanluis_stops:
            if stop_id == stop[0]:
                distTraveled = stop[11]
                print("dist: ", distTraveled)
                timeTraveledSinceLastStop = abs(float(distTraveled)/avg_bus_speed)
                time_diff = datetime.timedelta(hours=timeTraveledSinceLastStop)
                return time_diff
    elif shape_id == 'hacia_sanluis':
        for stop in hacia_sanluis_stops:
            if stop_id == stop[0]:
                distTraveled = stop[11]
                print("dist: ", distTraveled)
                timeTraveledSinceLastStop = abs(float(distTraveled)/avg_bus_speed)
                time_diff = datetime.timedelta(hours=timeTraveledSinceLastStop)
                return time_diff
    elif shape_id == 'desde_jorco':
        for stop in desde_jorco_stops:
            if stop_id == stop[0]:
                distTraveled = stop[11]
                print("dist: ", distTraveled)
                timeTraveledSinceLastStop = abs(float(distTraveled)/avg_bus_speed)
                time_diff = datetime.timedelta(hours=timeTraveledSinceLastStop)
                return time_diff
    elif shape_id == 'hacia_jorco':
        for stop in hacia_jorco_stops:
            if stop_id == stop[0]:
                distTraveled = stop[11]
                print("dist: ", distTraveled)
                timeTraveledSinceLastStop = abs(float(distTraveled)/avg_bus_speed)
                time_diff = datetime.timedelta(hours=timeTraveledSinceLastStop)
                return time_diff
    return datetime.timedelta(hours=0)
    pass


def getStartTime(trip_id):
    split = trip_id.split('_')
    time = split[3]
    time_obj = datetime.datetime.strptime(time, '%H:%M:%S')

    if (split[0] == 'desde' and (split[1] == 'sangabriel' or split[1] == 'turrujal' or split[1] == 'sanluis')):
        offset15min = datetime.timedelta(hours=00,minutes=15,seconds=00)
        time_obj = time_obj-offset15min
    return time_obj

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
    if (shape_id == 'desde_jorco'):
        route = ['JO', 'SJ']
    if (shape_id == 'hacia_hacia'):
        route = ['SJ', 'JO']
    return route



























read_shapes()
read_stops()

# TODO: HACER UNA FUNCION QUE LLAME TODAS ESTAS FUNCIONES AUTOMATICAMENTE
find_stops_in_shape(desde_sangabriel_shape, desde_sangabriel_stops)
find_stops_in_shape(desde_acosta_shape, desde_acosta_stops)
find_stops_in_shape(desde_turrujal_shape, desde_turrujal_stops)
find_stops_in_shape(desde_sanluis_shape, desde_sanluis_stops)
find_stops_in_shape(desde_jorco_shape, desde_jorco_stops)
find_stops_in_shape(hacia_sangabriel_shape, hacia_sangabriel_stops)
find_stops_in_shape(hacia_acosta_shape, hacia_acosta_stops)
find_stops_in_shape(hacia_turrujal_shape, hacia_turrujal_stops)
find_stops_in_shape(hacia_sanluis_shape, hacia_sanluis_stops)
find_stops_in_shape(hacia_jorco_shape, hacia_jorco_stops)


stop_times = getStopTimes(1)
with open("stop_times.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(stop_times)
