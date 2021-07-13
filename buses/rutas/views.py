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

    stops_from_SJ = {}
    stops_to_SJ = {}
    Coord1_to_SJ = {}
    Coord1_from_SJ = {}
    Coord2_to_SJ = {}
    Coord2_from_SJ = {}

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

    #######################################
    # 0
    Coord1_to_SJ['SanJose'] = []
    Coord1_to_SJ['Jorco'] = []
    Coord1_to_SJ['Mangos'] = []
    Coord1_to_SJ['SanGabriel'] = []
    Coord1_to_SJ['SanIgnacio'] = []
    Coord1_to_SJ['SanLuis'] = []
    Coord1_to_SJ['Turrujal'] = []

    # 1
    Coord1_from_SJ['SanJose'] = []
    Coord1_from_SJ['Jorco'] = []
    Coord1_from_SJ['Mangos'] = []
    Coord1_from_SJ['SanGabriel'] = []
    Coord1_from_SJ['SanIgnacio'] = []
    Coord1_from_SJ['SanLuis'] = []
    Coord1_from_SJ['Turrujal'] = []

    #######################################

    # 0
    Coord2_to_SJ['SanJose'] = []
    Coord2_to_SJ['Jorco'] = []
    Coord2_to_SJ['Mangos'] = []
    Coord2_to_SJ['SanGabriel'] = []
    Coord2_to_SJ['SanIgnacio'] = []
    Coord2_to_SJ['SanLuis'] = []
    Coord2_to_SJ['Turrujal'] = []
    Coord2_to_SJ['Orphans'] = []
    # 1
    Coord2_from_SJ['SanJose'] = []
    Coord2_from_SJ['Jorco'] = []
    Coord2_from_SJ['Mangos'] = []
    Coord2_from_SJ['SanGabriel'] = []
    Coord2_from_SJ['SanIgnacio'] = []
    Coord2_from_SJ['SanLuis'] = []
    Coord2_from_SJ['Turrujal'] = []
    Coord2_from_SJ['Orphans'] = []

    #####################################################################################

    for stop in Stop.objects.all():

        if stop.stop_id.find("SJ_0") != -1:
            Coord1_to_SJ['SanJose'].append(stop.lat)
        elif stop.stop_id.find("SJ_1") != -1:
            Coord1_from_SJ['SanJose'].append(stop.lat)

        elif stop.stop_id.find("LM_0") != -1:
            Coord1_to_SJ['Mangos'].append(stop.lat)
        elif stop.stop_id.find("LM_1") != -1:
            Coord1_from_SJ['Mangos'].append(stop.lat)

        elif stop.stop_id.find("SG_0") != -1:
            Coord1_to_SJ['SanGabriel'].append(stop.lat)
        elif stop.stop_id.find("SG_1") != -1:
            Coord1_from_SJ['SanGabriel'].append(stop.lat)

        elif stop.stop_id.find("SI_0") != -1:
            Coord1_to_SJ['SanIgnacio'].append(stop.lat)
        elif stop.stop_id.find("SI_1") != -1:
            Coord1_from_SJ['SanIgnacio'].append(stop.lat)

        elif stop.stop_id.find("SL_0") != -1:
            Coord1_to_SJ['SanLuis'].append(stop.lat)
        elif stop.stop_id.find("SL_1") != -1:
            Coord1_from_SJ['SanLuis'].append(stop.lat)

        elif stop.stop_id.find("TU_0") != -1:
            Coord1_to_SJ['Turrujal'].append(stop.lat)
        elif stop.stop_id.find("TU_1") != -1:
            Coord1_from_SJ['Turrujal'].append(stop.lat)

        elif stop.stop_id.find("JO_0") != -1:
            Coord1_to_SJ['Jorco'].append(stop.lat)
        elif stop.stop_id.find("JO_1") != -1:
            Coord1_from_SJ['Jorco'].append(stop.lat)

        else:
            Coord2_from_SJ['Orphans'].append(stop.lat)

    #####################################################################################

    for stop in Stop.objects.all():

        if stop.stop_id.find("SJ_0") != -1:
            Coord2_to_SJ['SanJose'].append(stop.lon)
        elif stop.stop_id.find("SJ_1") != -1:
            Coord2_from_SJ['SanJose'].append(stop.lon)

        elif stop.stop_id.find("LM_0") != -1:
            Coord2_to_SJ['Mangos'].append(stop.lon)
        elif stop.stop_id.find("LM_1") != -1:
            Coord2_from_SJ['Mangos'].append(stop.lon)

        elif stop.stop_id.find("SG_0") != -1:
            Coord2_to_SJ['SanGabriel'].append(stop.lon)
        elif stop.stop_id.find("SG_1") != -1:
            Coord2_from_SJ['SanGabriel'].append(stop.lon)

        elif stop.stop_id.find("SI_0") != -1:
            Coord2_to_SJ['SanIgnacio'].append(stop.lon)
        elif stop.stop_id.find("SI_1") != -1:
            Coord2_from_SJ['SanIgnacio'].append(stop.lon)

        elif stop.stop_id.find("SL_0") != -1:
            Coord2_to_SJ['SanLuis'].append(stop.lon)
        elif stop.stop_id.find("SL_1") != -1:
            Coord2_from_SJ['SanLuis'].append(stop.lon)

        elif stop.stop_id.find("TU_0") != -1:
            Coord2_to_SJ['Turrujal'].append(stop.lon)
        elif stop.stop_id.find("TU_1") != -1:
            Coord2_from_SJ['Turrujal'].append(stop.lon)

        elif stop.stop_id.find("JO_0") != -1:
            Coord2_to_SJ['Jorco'].append(stop.lon)
        elif stop.stop_id.find("JO_1") != -1:
            Coord2_from_SJ['Jorco'].append(stop.lon)

        else:
            Coord2_from_SJ['Orphans'].append(stop.lon)

    #####################################################################################

    for stop in Stop.objects.all():

        if stop.stop_id.find("SJ_0") != -1:
            stops_to_SJ['SanJose'].append(stop.name)
        elif stop.stop_id.find("SJ_1") != -1:
            stops_from_SJ['SanJose'].append(stop.name)

        elif stop.stop_id.find("LM_0") != -1:
            stops_to_SJ['Mangos'].append(stop.name)
        elif stop.stop_id.find("LM_1") != -1:
            stops_from_SJ['Mangos'].append(stop.name)

        elif stop.stop_id.find("SG_0") != -1:
            stops_to_SJ['SanGabriel'].append(stop.name)
        elif stop.stop_id.find("SG_1") != -1:
            stops_from_SJ['SanGabriel'].append(stop.name)

        elif stop.stop_id.find("SI_0") != -1:
            stops_to_SJ['SanIgnacio'].append(stop.name)
        elif stop.stop_id.find("SI_1") != -1:
            stops_from_SJ['SanIgnacio'].append(stop.name)

        elif stop.stop_id.find("SL_0") != -1:
            stops_to_SJ['SanLuis'].append(stop.name)
        elif stop.stop_id.find("SL_1") != -1:
            stops_from_SJ['SanLuis'].append(stop.name)

        elif stop.stop_id.find("TU_0") != -1:
            stops_to_SJ['Turrujal'].append(stop.name)
        elif stop.stop_id.find("TU_1") != -1:
            stops_from_SJ['Turrujal'].append(stop.name)

        elif stop.stop_id.find("JO_0") != -1:
            stops_to_SJ['Jorco'].append(stop.name)
        elif stop.stop_id.find("JO_1") != -1:
            stops_from_SJ['Jorco'].append(stop.name)

        else:
            stops_from_SJ['Orphans'].append(stop.name)

    #####################################################################################

    stops = Stop.objects.all()

    ParadasSJTar = stops_from_SJ['SanJose']
    ParadasTarSJ = stops_to_SJ['SanJose']
    ParadasTarJor = stops_from_SJ['Jorco']
    ParadasJorTar = stops_to_SJ['Jorco']
    ParadasJorSI = stops_from_SJ['SanIgnacio']
    ParadasSIJor = stops_to_SJ['SanIgnacio']
    ParadasSITur = stops_from_SJ['Turrujal']
    ParadasTurSI = stops_to_SJ['Turrujal']
    ParadasSISL = stops_from_SJ['SanLuis']
    ParadasSLSI = stops_to_SJ['SanLuis']
    ParadasTarSG = stops_from_SJ['SanGabriel']
    ParadasSGTar = stops_to_SJ['SanGabriel']
    ParadasSGLM = stops_from_SJ['Mangos']
    ParadasLMSG = stops_to_SJ['Mangos']

    Coord1SJTar = Coord1_from_SJ['SanJose']
    Coord1TarSJ = Coord1_to_SJ['SanJose']
    Coord1TarJor = Coord1_from_SJ['Jorco']
    Coord1JorTar = Coord1_to_SJ['Jorco']
    Coord1JorSI = Coord1_from_SJ['SanIgnacio']
    Coord1SIJor = Coord1_to_SJ['SanIgnacio']
    Coord1SITur = Coord1_from_SJ['Turrujal']
    Coord1TurSI = Coord1_to_SJ['Turrujal']
    Coord1SISL = Coord1_from_SJ['SanLuis']
    Coord1SLSI = Coord1_to_SJ['SanLuis']
    Coord1TarSG = Coord1_from_SJ['SanGabriel']
    Coord1SGTar = Coord1_to_SJ['SanGabriel']
    Coord1SGLM = Coord1_from_SJ['Mangos']
    Coord1LMSG = Coord1_to_SJ['Mangos']

    Coord2SJTar = Coord2_from_SJ['SanJose']
    Coord2TarSJ = Coord2_to_SJ['SanJose']
    Coord2TarJor = Coord2_from_SJ['Jorco']
    Coord2JorTar = Coord2_to_SJ['Jorco']
    Coord2JorSI = Coord2_from_SJ['SanIgnacio']
    Coord2SIJor = Coord2_to_SJ['SanIgnacio']
    Coord2SITur = Coord2_from_SJ['Turrujal']
    Coord2TurSI = Coord2_to_SJ['Turrujal']
    Coord2SISL = Coord2_from_SJ['SanLuis']
    Coord2SLSI = Coord2_to_SJ['SanLuis']
    Coord2TarSG = Coord2_from_SJ['SanGabriel']
    Coord2SGTar = Coord2_to_SJ['SanGabriel']
    Coord2SGLM = Coord2_from_SJ['Mangos']
    Coord2LMSG = Coord2_to_SJ['Mangos']

    ######################################################

    for i in range(0, len(Coord1SJTar)):
        Coord1SJTar[i] = str(Coord1SJTar[i])

    for i in range(0, len(Coord2SJTar)):
        Coord2SJTar[i] = str(Coord2SJTar[i])

    Coord1SJTar = [w.replace(',', '.') for w in Coord1SJTar]
    Coord2SJTar = [w.replace(',', '.') for w in Coord2SJTar]

    for i in range(0, len(Coord1TarSJ)):
        Coord1TarSJ[i] = str(Coord1TarSJ[i])

    for i in range(0, len(Coord2TarSJ)):
        Coord2TarSJ[i] = str(Coord2TarSJ[i])

    Coord1TarSJ = [w.replace(',', '.') for w in Coord1TarSJ]
    Coord2TarSJ = [w.replace(',', '.') for w in Coord2TarSJ]

    for i in range(0, len(Coord1TarJor)):
        Coord1TarJor[i] = str(Coord1TarJor[i])

    for i in range(0, len(Coord2TarJor)):
        Coord2TarJor[i] = str(Coord2TarJor[i])

    Coord1TarJor = [w.replace(',', '.') for w in Coord1TarJor]
    Coord2TarJor = [w.replace(',', '.') for w in Coord2TarJor]

    for i in range(0, len(Coord1JorTar)):
        Coord1JorTar[i] = str(Coord1JorTar[i])

    for i in range(0, len(Coord2JorTar)):
        Coord2JorTar[i] = str(Coord2JorTar[i])

    Coord1JorTar = [w.replace(',', '.') for w in Coord1JorTar]
    Coord2JorTar = [w.replace(',', '.') for w in Coord2JorTar]

    for i in range(0, len(Coord1JorSI)):
        Coord1JorSI[i] = str(Coord1JorSI[i])

    for i in range(0, len(Coord2JorSI)):
        Coord2JorSI[i] = str(Coord2JorSI[i])

    Coord1JorSI = [w.replace(',', '.') for w in Coord1JorSI]
    Coord2JorSI = [w.replace(',', '.') for w in Coord1JorSI]

    for i in range(0, len(Coord1SIJor)):
        Coord1SIJor[i] = str(Coord1SIJor[i])

    for i in range(0, len(Coord2SIJor)):
        Coord2SIJor[i] = str(Coord2SIJor[i])

    Coord1SIJor = [w.replace(',', '.') for w in Coord1SIJor]
    Coord2SIJor = [w.replace(',', '.') for w in Coord2SIJor]

    for i in range(0, len(Coord1SITur)):
        Coord1SITur[i] = str(Coord1SITur[i])

    for i in range(0, len(Coord2SITur)):
        Coord2SITur[i] = str(Coord2SITur[i])

    Coord1SITur = [w.replace(',', '.') for w in Coord1SITur]
    Coord2SITur = [w.replace(',', '.') for w in Coord2SITur]

    for i in range(0, len(Coord1TurSI)):
        Coord1TurSI[i] = str(Coord1TurSI[i])

    for i in range(0, len(Coord2TurSI)):
        Coord2TurSI[i] = str(Coord2TurSI[i])

    Coord1TurSI = [w.replace(',', '.') for w in Coord1TurSI]
    Coord2TurSI = [w.replace(',', '.') for w in Coord2TurSI]

    for i in range(0, len(Coord1SISL)):
        Coord1SISL[i] = str(Coord1SISL[i])

    for i in range(0, len(Coord2SISL)):
        Coord2SISL[i] = str(Coord2SISL[i])

    Coord1SISL = [w.replace(',', '.') for w in Coord1SISL]
    Coord2SISL = [w.replace(',', '.') for w in Coord2SISL]

    for i in range(0, len(Coord1SLSI)):
        Coord1SLSI[i] = str(Coord1SLSI[i])

    for i in range(0, len(Coord2SLSI)):
        Coord2SLSI[i] = str(Coord2SLSI[i])

    Coord1SLSI = [w.replace(',', '.') for w in Coord1SLSI]
    Coord2SLSI = [w.replace(',', '.') for w in Coord2SLSI]

    for i in range(0, len(Coord1TarSG)):
        Coord1TarSG[i] = str(Coord1TarSG[i])

    for i in range(0, len(Coord2TarSG)):
        Coord2TarSG[i] = str(Coord2TarSG[i])

    Coord1TarSG = [w.replace(',', '.') for w in Coord1TarSG]
    Coord2TarSG = [w.replace(',', '.') for w in Coord2TarSG]

    for i in range(0, len(Coord1SGTar)):
        Coord1SGTar[i] = str(Coord1SGTar[i])

    for i in range(0, len(Coord2SGTar)):
        Coord2SGTar[i] = str(Coord2SGTar[i])

    Coord1SGTar = [w.replace(',', '.') for w in Coord1SGTar]
    Coord2SGTar = [w.replace(',', '.') for w in Coord2SGTar]

    for i in range(0, len(Coord1SGLM)):
        Coord1SGLM[i] = str(Coord1SGLM[i])

    for i in range(0, len(Coord2SGLM)):
        Coord2SGLM[i] = str(Coord2SGLM[i])

    Coord1SGLM = [w.replace(',', '.') for w in Coord1SGLM]
    Coord2SGLM = [w.replace(',', '.') for w in Coord2SGLM]

    for i in range(0, len(Coord1LMSG)):
        Coord1LMSG[i] = str(Coord1LMSG[i])

    for i in range(0, len(Coord2LMSG)):
        Coord2LMSG[i] = str(Coord2LMSG[i])

    Coord1LMSG = [w.replace(',', '.') for w in Coord1LMSG]
    Coord2LMSG = [w.replace(',', '.') for w in Coord2LMSG]

    ######################################################

    MatInfoSJTar = zip(ParadasSJTar, Coord1SJTar, Coord2SJTar)
    MatInfoSJTar2 = zip(ParadasSJTar, Coord1SJTar, Coord2SJTar)
    MatInfoSJTar3 = zip(ParadasSJTar, Coord1SJTar, Coord2SJTar)
    MatInfoTarSJ = zip(ParadasTarSJ, Coord1TarSJ, Coord2TarSJ)
    MatInfoTarSJ2 = zip(ParadasTarSJ, Coord1TarSJ, Coord2TarSJ)
    MatInfoTarSJ3 = zip(ParadasTarSJ, Coord1TarSJ, Coord2TarSJ)
    MatInfoTarJor = zip(ParadasTarJor, Coord1TarJor, Coord2TarJor)
    MatInfoTarJor2 = zip(ParadasTarJor, Coord1TarJor, Coord2TarJor)
    MatInfoJorTar = zip(ParadasJorTar, Coord1JorTar, Coord2JorTar)
    MatInfoJorTar2 = zip(ParadasJorTar, Coord1JorTar, Coord2JorTar)
    MatInfoJorSI = zip(ParadasJorSI, Coord1JorSI, Coord2JorSI)
    MatInfoJorSI2 = zip(ParadasJorSI, Coord1JorSI, Coord2JorSI)
    MatInfoSIJor = zip(ParadasSIJor, Coord1SIJor, Coord2SIJor)
    MatInfoSIJor2 = zip(ParadasSIJor, Coord1SIJor, Coord2SIJor)
    MatInfoSITur = zip(ParadasSITur, Coord1SITur, Coord2SITur)
    MatInfoTurSI = zip(ParadasTurSI, Coord1TurSI, Coord2TurSI)
    MatInfoSISL = zip(ParadasSISL, Coord1SISL, Coord2SISL)
    MatInfoSLSI = zip(ParadasSLSI, Coord1SLSI, Coord2SLSI)
    MatInfoTarSG = zip(ParadasTarSG, Coord1TarSG, Coord2TarSG)
    MatInfoSGTar = zip(ParadasSGTar, Coord1SGTar, Coord2SGTar)
    MatInfoSGLM = zip(ParadasSGLM, Coord1SGLM, Coord2SGLM)
    MatInfoLMSG = zip(ParadasLMSG, Coord1LMSG, Coord2LMSG)

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
        'stops_from_SJ' : stops_from_SJ,
        'stops_to_SJ' : stops_to_SJ,

        'MatInfoSJTar' : MatInfoSJTar,
        'MatInfoSJTar2': MatInfoSJTar2,
        'MatInfoSJTar3': MatInfoSJTar3,
        'MatInfoTarSJ' : MatInfoTarSJ,
        'MatInfoTarSJ2': MatInfoTarSJ2,
        'MatInfoTarSJ3': MatInfoTarSJ3,
        'MatInfoTarJor' : MatInfoTarJor,
        'MatInfoTarJor2': MatInfoTarJor2,
        'MatInfoJorTar' : MatInfoJorTar,
        'MatInfoJorTar2': MatInfoJorTar2,
        'MatInfoJorSI' : MatInfoJorSI,
        'MatInfoJorSI2': MatInfoJorSI2,
        'MatInfoSIJor' : MatInfoSIJor,
        'MatInfoSIJor2': MatInfoSIJor2,
        'MatInfoSITur' : MatInfoSITur,
        'MatInfoTurSI' : MatInfoTurSI,
        'MatInfoSISL' : MatInfoSISL,
        'MatInfoSLSI' : MatInfoSLSI,
        'MatInfoTarSG' : MatInfoTarSG,
        'MatInfoSGTar' : MatInfoSGTar,
        'MatInfoSGLM' : MatInfoSGLM,
        'MatInfoLMSG' : MatInfoLMSG,
    }

    return render(request, 'ruta.html', context)
