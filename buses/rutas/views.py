from django.shortcuts import get_object_or_404, render
from .models import Route, Shape, Calendar, Trip, Stop, StopTime, CalendarDate
from datetime import datetime
from itertools import zip_longest

''' CHUECA Function to execute when user goes to /rutas '''
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

    return render(request, 'rutas.html', context)

# Esta sí es

def ruta(request, url_ruta):
    ''' Función para mostrar la información de cada ruta.
    Opciones:
    - San Gabriel
    - Acosta con sus diferentes ramales
    '''

    # Obtener la información de la ruta consultada
    ''' Valores:
    route_id, agency, short_name, long_name, desc, 
    route_type, url, color, text_color
    '''
    route = get_object_or_404(Route, url=url_ruta)

    # Extraer los viajes asociados con esta ruta para cada servicio y en cada dirección
    ''' Valores:
    route, service,	trip_id, trip_headsign, trip_short_name, 
    direction (0: hacia San José, 1: desde San José), shape, 
    wheelchair_accessible, bikes_allowed
    '''
    trips_entresemana_0 = Trip.objects.filter(
                route=route,
                service=Calendar.objects.get(service_id='entresemana'),
                direction='0')
    trips_entresemana_1 = Trip.objects.filter(
                route=route,
                service=Calendar.objects.get(service_id='entresemana'),
                direction='1')
    trips_sabado_0 = Trip.objects.filter(
                route=route,
                service=Calendar.objects.get(service_id='sabado'),
                direction='0')
    trips_sabado_1 = Trip.objects.filter(
                route=route,
                service=Calendar.objects.get(service_id='sabado'),
                direction='1')
    trips_domingo_0 = Trip.objects.filter(
                route=route,
                service=Calendar.objects.get(service_id='domingo'),
                direction='0')
    trips_domingo_1 = Trip.objects.filter(
                route=route,
                service=Calendar.objects.get(service_id='domingo'),
                direction='1')

    # Entre semana

    para_ordenar = []
    for i in trips_entresemana_0:
        viaje = StopTime.objects.get(trip=i)
        para_ordenar.append([viaje.departure_time, str(i.shape)])
    
    para_ordenar.sort()
    horario_entresemana_0 = [i[0] for i in para_ordenar]
    ramales_entresemana_0 = [i[1] for i in para_ordenar]

    para_ordenar = []
    for i in trips_entresemana_1:
        viaje = StopTime.objects.get(trip=i)
        para_ordenar.append([viaje.departure_time, str(i.shape)])

    para_ordenar.sort()
    horario_entresemana_1 = [i[0] for i in para_ordenar]
    ramales_entresemana_1 = [i[1] for i in para_ordenar]
    
    horario_entresemana = zip_longest(
                          [i.strftime("%-I:%M %p") for i in horario_entresemana_0],
                          ramales_entresemana_0,
                          [i.strftime("%-I:%M %p") for i in horario_entresemana_1],
                          ramales_entresemana_1,
                          fillvalue='-')

    # Sábado

    para_ordenar = []
    for i in trips_sabado_0:
        viaje = StopTime.objects.get(trip=i)
        para_ordenar.append([viaje.departure_time, str(i.shape)])

    para_ordenar.sort()
    horario_sabado_0 = [i[0] for i in para_ordenar]
    ramales_sabado_0 = [i[1] for i in para_ordenar]

    para_ordenar = []
    for i in trips_sabado_1:
        viaje = StopTime.objects.get(trip=i)
        para_ordenar.append([viaje.departure_time, str(i.shape)])

    para_ordenar.sort()
    horario_sabado_1 = [i[0] for i in para_ordenar]
    ramales_sabado_1 = [i[1] for i in para_ordenar]

    horario_sabado = zip_longest(
                        [i.strftime("%-I:%M %p") for i in horario_sabado_0], 
                        ramales_sabado_0,
                        [i.strftime("%-I:%M %p") for i in horario_sabado_1],
                        ramales_sabado_1,
                        fillvalue='-')

   # Domingo

    para_ordenar = []
    for i in trips_domingo_0:
        viaje = StopTime.objects.get(trip=i)
        para_ordenar.append([viaje.departure_time, str(i.shape)])

    para_ordenar.sort()
    horario_domingo_0 = [i[0] for i in para_ordenar]
    ramales_domingo_0 = [i[1] for i in para_ordenar]

    para_ordenar = []
    for i in trips_domingo_1:
        viaje = StopTime.objects.get(trip=i)
        para_ordenar.append([viaje.departure_time, str(i.shape)])

    para_ordenar.sort()
    horario_domingo_1 = [i[0] for i in para_ordenar]
    ramales_domingo_1 = [i[1] for i in para_ordenar]

    horario_domingo = zip_longest(
                        [i.strftime("%-I:%M %p") for i in horario_domingo_0],
                        ramales_domingo_0, 
                        [i.strftime("%-I:%M %p") for i in horario_domingo_1],
                        ramales_domingo_1,
                        fillvalue='-')

    # Momento actual

    ahora = datetime.now()
    # ahora = datetime(2020, 11, 21, 11, 32, 52, 978416)
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    fecha = [dias[ahora.weekday()], ahora.day, meses[ahora.month - 1], ahora.year]

    # Próximo bus
    
    if ahora.weekday() <= 4:
        horario_0 = horario_entresemana_0
        ramales_0 = ramales_entresemana_0
        horario_1 = horario_entresemana_1
        ramales_1 = ramales_entresemana_1
        horario_activo = ['active', '', '', 'true', 'false', 'false', 'show active', '', '']
    elif ahora.weekday() == 5:
        horario_0 = horario_sabado_0
        ramales_0 = ramales_sabado_0
        horario_1 = horario_sabado_1
        ramales_1 = ramales_sabado_1
        horario_activo = ['', 'active', '', 'false', 'true', 'false', '', 'show active', '']
    else:
        horario_0 = horario_domingo_0
        ramales_0 = ramales_domingo_0
        horario_1 = horario_domingo_1
        ramales_1 = ramales_domingo_1
        horario_activo = ['', '', 'active', 'false', 'false', 'true', '', '', 'show active']

    proximos_hacia_sanjose = [[i[0].strftime("%-I:%M %p"), str(i[1])] for i in proximo_bus(horario_0, ramales_0, ahora)]
    proximos_desde_sanjose = [[i[0].strftime("%-I:%M %p"), str(i[1])] for i in proximo_bus(horario_1, ramales_1, ahora)]

    # Feriados

    feriados = CalendarDate.objects.filter(exception_type='1')

    context = {
        'route': route, 
        'fecha': fecha,
        'horario_entresemana': horario_entresemana,
        'horario_sabado': horario_sabado,
        'horario_domingo': horario_domingo,
        'horario_activo': horario_activo,
        'proximos_hacia_sanjose': proximos_hacia_sanjose,
        'proximos_desde_sanjose': proximos_desde_sanjose,
        'feriados': feriados,
    }

    return render(request, 'ruta.html', context)

def proximo_bus(horario, ramales, ahora):
    '''Regresa una lista (datetime) de las próximas tres horas
    de salida a partir de ahora dado un horario específico
    '''
    
    # Inicializar lista de próximos buses (horas de salida)
    proximos = []

    salidas = iter(horario)     # horas de salidas iterables
    next(salidas)               # primera hora de salida

    # Recorrer cada hora de salida del horario
    for i, salida in enumerate(horario):
        proximo_1 = salida

        if ahora.hour == salida.hour:
            if ahora.minute < salida.minute:
                proximos.append([proximo_1, ramales[i]])
                try:
                    proximo_2 = next(salidas)
                    proximos.append([proximo_2, ramales[i+1]])

                    proximo_3 = next(salidas)
                    proximos.append([proximo_3, ramales[i+2]])
                except:
                    break
                return proximos
        
        elif ahora.hour <= salida.hour:
            proximos.append([proximo_1, ramales[i]])
            try:
                proximo_2 = next(salidas)
                proximos.append([proximo_2, ramales[i+1]])

                proximo_3 = next(salidas)
                proximos.append([proximo_3, ramales[i+2]])
            except:
                break
            return proximos
        
        try:
            next(salidas)
        except:
            break
    
    return proximos

def proximo_bus_widget(request, url_ruta):

    return render(request, 'proximobus.html')
