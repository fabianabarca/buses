from django.shortcuts import get_object_or_404, render
from .models import FareAttribute, Route, Shape, Calendar, Trip, Stop, StopTime, CalendarDate, FeedInfo
from datetime import datetime
from itertools import zip_longest
from django.conf import settings
from django.db.models import Q


def rutas(request):
    rutas = Route.objects.all()
    ahora = datetime.now()
    meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
    dias = ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo')
    fecha = [dias[ahora.weekday()], ahora.day, meses[ahora.month - 1], ahora.year]

    context = {
        'rutas': rutas, # Lista de rutas
        'fecha': fecha
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
    if url_ruta == 'sangabriel':
        route = get_object_or_404(Route, route_id='SGAB')
        route_id_array = ['SGAB', 'SGAB']
    elif url_ruta == 'acosta':
        route = get_object_or_404(Route, route_id='ACOS')
        route_id_array = ['ACOS', 'TURR']

    # Extraer los viajes asociados con esta ruta para cada servicio y en cada dirección
    ''' Valores:
    route, service,	trip_id, trip_headsign, trip_short_name,
    direction (0: hacia San José, 1: desde San José), shape,
    wheelchair_accessible, bikes_allowed
    '''

    horario_entresemana_0, ramales_entresemana_0 = Trip.objects.horario_y_ramales(
        route_id_array=route_id_array,
        service_id='entresemana',
        direction='0')

    horario_entresemana_1, ramales_entresemana_1 = Trip.objects.horario_y_ramales(
        route_id_array=route_id_array,
        service_id='entresemana',
        direction='1')

    horario_sabado_0, ramales_sabado_0 = Trip.objects.horario_y_ramales(
        route_id_array=route_id_array,
        service_id='sabado',
        direction='0')

    horario_sabado_1, ramales_sabado_1 = Trip.objects.horario_y_ramales(
        route_id_array=route_id_array,
        service_id='sabado',
        direction='1')

    horario_domingo_0, ramales_domingo_0 = Trip.objects.horario_y_ramales(
        route_id_array=route_id_array,
        service_id='domingo',
        direction='0')

    horario_domingo_1, ramales_domingo_1 = Trip.objects.horario_y_ramales(
        route_id_array=route_id_array,
        service_id='domingo',
        direction='1')


    # Entre semana
    horario_entresemana = zip_longest(
                          [i.strftime("%I:%M %p") for i in horario_entresemana_0],
                          ramales_entresemana_0,
                          [i.strftime("%I:%M %p") for i in horario_entresemana_1],
                          ramales_entresemana_1,
                          fillvalue='-')

    # Sábado
    horario_sabado = zip_longest(
                        [i.strftime("%I:%M %p") for i in horario_sabado_0],
                        ramales_sabado_0,
                        [i.strftime("%I:%M %p") for i in horario_sabado_1],
                        ramales_sabado_1,
                        fillvalue='-')

   # Domingo
    horario_domingo = zip_longest(
                        [i.strftime("%I:%M %p") for i in horario_domingo_0],
                        ramales_domingo_0,
                        [i.strftime("%I:%M %p") for i in horario_domingo_1],
                        ramales_domingo_1,
                        fillvalue='-')

    # Momento actual

    ahora = datetime.now()
    # ahora = datetime(2020, 11, 21, 22, 32, 52, 978416)
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    fecha = [dias[ahora.weekday()], ahora.day, meses[ahora.month - 1], ahora.year]

    # Próximo bus

    if ahora.weekday() <= 4:
        horario_0 = horario_entresemana_0
        ramales_0 = ramales_entresemana_0
        horario_1 = horario_entresemana_1
        ramales_1 = ramales_entresemana_1
    elif ahora.weekday() == 5:
        horario_0 = horario_sabado_0
        ramales_0 = ramales_sabado_0
        horario_1 = horario_sabado_1
        ramales_1 = ramales_sabado_1
    else:
        horario_0 = horario_domingo_0
        ramales_0 = ramales_domingo_0
        horario_1 = horario_domingo_1
        ramales_1 = ramales_domingo_1

    ramales_0_acronimo = [
        element.replace('desde_','')
        .replace('hacia_','')
        .replace('turrujal','TU')
        .replace('sanluis','SL')
        .replace('jorco','JO')
        .replace('sangabriel','SG')
        .replace('acosta','AC')
        for element in ramales_0 ]

    ramales_1_acronimo = [
        element.replace('desde_','')
        .replace('hacia_','')
        .replace('turrujal','TU')
        .replace('sanluis','SL')
        .replace('jorco','JO')
        .replace('sangabriel','SG')
        .replace('acosta','AC')
        for element in ramales_1 ]

    # Tiempo en minutos, hora, minuto, acronimo del ramal
    horario_js_hacia_sanjose = [[i.hour *60 + i.minute, i.hour, i.minute, j] for i,j in zip(horario_0, ramales_0_acronimo)]
    horario_js_desde_sanjose = [[i.hour *60 + i.minute, i.hour, i.minute, j] for i,j in zip(horario_1, ramales_1_acronimo)]

    # Feriados

    feriados = CalendarDate.objects.filter(exception_type='1')

    # Actualización de información del suministro

    informacion = FeedInfo.objects.get(pk=1)

    # Tarifas

    tarifas = FareAttribute.objects.filter(fare_id__startswith=route_id_array[0]).union(FareAttribute.objects.filter(fare_id__startswith=route_id_array[1])).order_by('-price')

    # Paradas de buses

    # Paradas
    stops_from_SJ = {}
    stops_to_SJ = {}

    # 0
    stops_to_SJ['SanJose'] = []
    stops_to_SJ['Jorco'] = []
    stops_to_SJ['Mangos'] = []
    stops_to_SJ['SanGabriel'] = []
    stops_to_SJ['SanIgnacio'] = []
    stops_to_SJ['SanLuis'] = []
    stops_to_SJ['Turrujal'] = []

    # 1
    stops_from_SJ['SanJose'] = []
    stops_from_SJ['Jorco'] = []
    stops_from_SJ['Mangos'] = []
    stops_from_SJ['SanGabriel'] = []
    stops_from_SJ['SanIgnacio'] = []
    stops_from_SJ['SanLuis'] = []
    stops_from_SJ['Turrujal'] = []
    stops_from_SJ['Orphans'] = []

    for stop in Stop.objects.all():

        if stop.stop_id.find("SJ_0") != -1:
            stops_to_SJ['SanJose'].append(stop)
        elif stop.stop_id.find("SJ_1") != -1:
            stops_from_SJ['SanJose'].append(stop)

        elif stop.stop_id.find("LM_0") != -1:
            stops_to_SJ['Mangos'].append(stop)
        elif stop.stop_id.find("LM_1") != -1:
            stops_from_SJ['Mangos'].append(stop)

        elif stop.stop_id.find("SG_0") != -1:
            stops_to_SJ['SanGabriel'].append(stop)
        elif stop.stop_id.find("SG_1") != -1:
            stops_from_SJ['SanGabriel'].append(stop)

        elif stop.stop_id.find("SI_0") != -1:
            stops_to_SJ['SanIgnacio'].append(stop)
        elif stop.stop_id.find("SI_1") != -1:
            stops_from_SJ['SanIgnacio'].append(stop)

        elif stop.stop_id.find("SL_0") != -1:
            stops_to_SJ['SanLuis'].append(stop)
        elif stop.stop_id.find("SL_1") != -1:
            stops_from_SJ['SanLuis'].append(stop)

        elif stop.stop_id.find("TU_0") != -1:
            stops_to_SJ['Turrujal'].append(stop)
        elif stop.stop_id.find("TU_1") != -1:
            stops_from_SJ['Turrujal'].append(stop)

        elif stop.stop_id.find("JO_0") != -1:
            stops_to_SJ['Jorco'].append(stop)
        elif stop.stop_id.find("JO_1") != -1:
            stops_from_SJ['Jorco'].append(stop)

        else:
            stops_from_SJ['Orphans'].append(stop)

    stops = Stop.objects.all()

    context = {
        'maxBounds': settings.RUTAS_MAP_MAX_BOUNDS,
        'route': route,
        'fecha': fecha,
        'horario_entresemana': horario_entresemana,
        'horario_sabado': horario_sabado,
        'horario_domingo': horario_domingo,
        'horario_js_hacia_sanjose': horario_js_hacia_sanjose,
        'horario_js_desde_sanjose': horario_js_desde_sanjose,
        'feriados': feriados,
        'informacion': informacion,
        'tarifas': tarifas,
        # Parte de la solución horrible
        'stops_from_SJ': stops_from_SJ,
        'stops_to_SJ': stops_to_SJ,
        'ParadasSJTar': stops_from_SJ['SanJose'],
        'ParadasTarSJ': stops_to_SJ['SanJose'],
        'ParadasTarJor': stops_from_SJ['Jorco'],
        'ParadasJorTar': stops_to_SJ['Jorco'],
        'ParadasJorSI': stops_from_SJ['SanIgnacio'],
        'ParadasSIJor': stops_to_SJ['SanIgnacio'],
        'ParadasSITur': stops_from_SJ['Turrujal'],
        'ParadasTurSI': stops_to_SJ['Turrujal'],
        'ParadasSISL': stops_from_SJ['SanLuis'],
        'ParadasSLSI': stops_to_SJ['SanLuis'],
        'ParadasTarSG': stops_from_SJ['SanGabriel'],
        'ParadasSGTar': stops_to_SJ['SanGabriel'],
        'ParadasSGLM': stops_from_SJ['Mangos'],
        'ParadasLMSG': stops_to_SJ['Mangos'],
    }

    return render(request, 'ruta.html', context)
