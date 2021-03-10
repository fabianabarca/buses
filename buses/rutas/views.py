from django.shortcuts import get_object_or_404, render
from .models import Route, Shape, Calendar, Trip, Stop, StopTime, CalendarDate
from datetime import datetime
from itertools import zip_longest

def rutas(request):
    rutas = Route.objects.all()
    
    ahora = datetime.now()
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    fecha = [dias[ahora.weekday()], ahora.day, meses[ahora.month - 1], ahora.year]

    context = {
        'rutas': rutas, # Lista de rutas  
        'fecha': fecha,
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
