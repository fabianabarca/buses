from django.shortcuts import get_object_or_404, render
from .models import FareAttribute, Route, Shape, Calendar, Trip, Stop, StopTime, CalendarDate, FeedInfo
from datetime import datetime
from itertools import zip_longest
from django.conf import settings
from django.db.models import Q

'''
@param: ninguno
@description: funcion auxiliar para obtener contexto de tiempo
@returns: objeto fecha con contexto temporal
'''
def obtenerFecha():
    ahora = datetime.now()
    meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
    dias = ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo')
    return [dias[ahora.weekday()], ahora.day, meses[ahora.month - 1], ahora.year]

'''
@param: http request
@description: define contexto de tiempo y rutas para pagina html de rutas
@returns: html render del request
'''
def rutas(request):
    rutas = Route.objects.all()
    context = {
        'rutas': rutas,
        'fecha': obtenerFecha()
    }
    return render(request, 'rutas.html', context)


'''
@param: recibe url con el id de la ruta, 'sangabriel' o 'acosta'
@description: escoje la ruta basado en el url y devuelve valores de ambiente
Valores: (documentación previa)
route_id, agency, short_name, long_name, desc,
route_type, url, color, text_color
@returns: arreglo con los códigos de las rutas y objeto ruta
'''
def obtenerInfoRuta(url_ruta):
    if url_ruta == 'sangabriel':
        route = get_object_or_404(Route, route_id='SGAB')
        route_id_array = ['SGAB', 'SGAB']
    elif url_ruta == 'acosta':
        route = get_object_or_404(Route, route_id='ACOS')
        route_id_array = ['ACOS', 'TURR']
    return route_id_array, route

'''
@param: arreglo con los ids de la ruta
@description: obtiene de GTFS el trip en formato .txt
@returns: horarios de las rutas entre semana
'''
def obtenerViajesEntreSemana(route_id_array):
    horario_entresemana_0, ramales_entresemana_0 = Trip.objects.horario_y_ramales(route_id_array=route_id_array,service_id='entresemana',direction='0')
    horario_entresemana_1, ramales_entresemana_1 = Trip.objects.horario_y_ramales(route_id_array=route_id_array,service_id='entresemana',direction='1')
    return horario_entresemana_0, ramales_entresemana_0, horario_entresemana_1, ramales_entresemana_1

def obtenerViajesSabado(route_id_array):
    horario_sabado_0, ramales_sabado_0 = Trip.objects.horario_y_ramales(route_id_array=route_id_array,service_id='sabado',direction='0')
    horario_sabado_1, ramales_sabado_1 = Trip.objects.horario_y_ramales(route_id_array=route_id_array,service_id='sabado',direction='1')
    return horario_sabado_0, ramales_sabado_0, horario_sabado_1, ramales_sabado_1

def obtenerViajesDomingo(route_id_array):
    horario_domingo_0, ramales_domingo_0 = Trip.objects.horario_y_ramales(route_id_array=route_id_array,service_id='domingo',direction='0')
    horario_domingo_1, ramales_domingo_1 = Trip.objects.horario_y_ramales(route_id_array=route_id_array,service_id='domingo',direction='1')
    return horario_domingo_0, ramales_domingo_0, horario_domingo_1, ramales_domingo_1

'''s
@param: http request, url de la ruta
@description: muestra la informacion de cada ruta, san gabriel o acosta-ramales
@returns: render de la pagina con las rutas obtenidas
'''
def ruta(request, url_ruta):
    route_id_array, route = obtenerInfoRuta(url_ruta)
    # Extraer los viajes asociados con esta ruta para cada servicio y en cada dirección
    ''' Valores:
    route, service,	trip_id, trip_headsign, trip_short_name,
    direction (0: hacia San José, 1: desde San José), shape,
    wheelchair_accessible, bikes_allowed
    '''
    horario_entresemana_0, ramales_entresemana_0, horario_entresemana_1, ramales_entresemana_1 = obtenerViajesEntreSemana(route_id_array)
    horario_sabado_0, ramales_sabado_0, horario_sabado_1, ramales_sabado_1 = obtenerViajesSabado(route_id_array)
    horario_domingo_0, ramales_domingo_0, horario_domingo_1, ramales_domingo_1 = obtenerViajesDomingo(route_id_array)
    
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
    fecha = obtenerFecha() 

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

    if url_ruta == 'sangabriel':
        desde = ['LM_0', 'SG_0', 'SJ_0']
        hacia = ['SJ_1', 'SG_1', 'LM_1']        
    elif url_ruta == 'acosta':
        desde = ['SI_0', 'JO_0', 'SJ_0']
        hacia = ['SJ_1', 'JO_1', 'SI_1']
    
    #paradas_desde = Stop.objects.filter(stop_id__startswith=desde[0]).union(Stop.objects.filter(stop_id__startswith=desde[1])).union(Stop.objects.filter(stop_id__startswith=desde[2]))
    #paradas_desde = Stop.objects.filter(Q(stop_id__startswith=desde[0]) | Q(stop_id__startswith=desde[1]) | Q(stop_id__startswith=desde[2]))
    #paradas_hacia = Stop.objects.filter(stop_id__startswith=hacia[0]).union(Stop.objects.filter(stop_id__startswith=hacia[1])).union(Stop.objects.filter(stop_id__startswith=hacia[2]))
    #paradas_hacia = Stop.objects.filter(Q(stop_id__startswith=hacia[0]) | Q(stop_id__startswith=hacia[1]) | Q(stop_id__startswith=hacia[2])).order_by('pk')
    
    # Solución horrible (terrible, terrible)
    paradas_desde_0 = Stop.objects.filter(stop_id__startswith=desde[0])
    paradas_desde_1 = Stop.objects.filter(stop_id__startswith=desde[1])
    paradas_desde_2 = Stop.objects.filter(stop_id__startswith=desde[2])
    paradas_hacia_0 = Stop.objects.filter(stop_id__startswith=hacia[0])
    paradas_hacia_1 = Stop.objects.filter(stop_id__startswith=hacia[1])
    paradas_hacia_2 = Stop.objects.filter(stop_id__startswith=hacia[2])

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
        'paradas_desde_0': paradas_desde_0,
        'paradas_desde_1': paradas_desde_1,
        'paradas_desde_2': paradas_desde_2,
        'paradas_hacia_0': paradas_hacia_0,
        'paradas_hacia_1': paradas_hacia_1,
        'paradas_hacia_2': paradas_hacia_2,
    }

    return render(request, 'ruta.html', context)
