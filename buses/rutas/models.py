from django.shortcuts import get_object_or_404
from django.db import models

## Managers

class tripManager(models.Manager):
    def horario_y_ramales(self, service_id='', route_id_array=[], direction=0):
        trips = super().get_queryset().filter(
            service__service_id=service_id,
            route__route_id__in = route_id_array,
            direction=direction
        )

        para_ordenar = []
        terminales = ['SJ_1_00', 'SG_0_00', 'SI_0_00']
        for i in trips:
            """
            if str(i.shape) == 'desde_jorco':
                viaje = StopTime.objects.get(trip=i, stop='JO_0_00')
            else:
                viaje = StopTime.objects.get(trip=i, stop__in=terminales)
            """
            para_ordenar.append([i.departure_time, str(i.shape)])

        para_ordenar.sort()
        horario = [i[0] for i in para_ordenar]
        ramales = [i[1] for i in para_ordenar]
        return (horario, ramales)

## Models

class Agency(models.Model):
    """One or more transit agencies that provide the data in this feed.
    Maps to agency.txt in the GTFS feed.
    """
    agency_id = models.CharField(
        primary_key=True,
        max_length=255, blank=True, db_index=True,
        help_text="Identificador único de la agencia de transportes.")
    name = models.CharField(
        max_length=255,
        help_text="Nombre completo de la agencia de transportes.")
    url = models.URLField(
        blank=True, help_text="URL de la agencia de transportes.")
    timezone = models.CharField(
        max_length=255,
        help_text="Zona horaria de la agencia de transportes.")
    lang = models.CharField(
        max_length=2, blank=True,
        help_text="Código ISO 639-1 de idioma primario.")
    phone = models.CharField(
        max_length=255, blank=True,
        help_text="Número de teléfono.")
    fare_url = models.URLField(
        blank=True, help_text="URL para la compra de tiquetes en línea.")
    email = models.EmailField(max_length=254,  blank=True, help_text="Correo electrónico de servicio al cliente.")

    class Meta:
        verbose_name = "agency"
        verbose_name_plural = "agencies"

    def __str__(self):
        return self.name

class Stop(models.Model):
    """A stop or station
    Maps to stops.txt in the GTFS feed.
    """
    stop_id = models.CharField(
        primary_key=True,
        max_length=255, db_index=True,
        help_text="Identificador único de una parada o estación.")
    name = models.CharField(
        max_length=255,
        help_text="Nombre de la parada.")
    desc = models.CharField(
        "description",
        max_length=255, blank=True,
        help_text='Descripción de la parada.')
    lat = models.DecimalField(
        max_digits=22,
        decimal_places=16,
        help_text='Latitud WGS 84 de la parada o estación.')
    lon = models.DecimalField(
        max_digits=22,
        decimal_places=16,
        help_text='Longitud WGS 84 de la parada o estación.')
    zone = models.ForeignKey(
        'Zone', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="Zona tarifaria para esta parada.") 
    url = models.URLField(
        blank=True, help_text="URL de la parada.")
    location_type = models.CharField(
        max_length=1, blank=True, choices=(('0', 'Parada'), ('1', 'Estación')),
        help_text="¿Es una parada o una estación?")
    parent_station = models.CharField(
        max_length=255, null=True, blank=True,
        help_text="La estación asociada con la parada.")
    wheelchair_boarding = models.CharField(
        max_length=1, null=True, blank=True,
        choices=(
            ('0', 'No hay información.'),
            ('1', 'Abordaje parcial de silla de ruedas.'),
            ('2', 'Las sillas de ruedas no pueden subir.')),
        help_text='¿Es posible subir al transporte en silla de ruedas?')

    class Meta:
        verbose_name = "stop"
        verbose_name_plural = "stops"

    def __str__(self):
        return self.stop_id + ': ' + self.name

class Route(models.Model):
    """A transit route
    Maps to route.txt in the GTFS feed.
    """
    route_id = models.CharField(
        primary_key=True,
        max_length=64, db_index=True,
        help_text="Identificador único de la ruta.")
    agency = models.ForeignKey(
        'Agency', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="Agencia de transportes de la ruta.")
    short_name = models.CharField(
        max_length=63,
        help_text="Nombre corto de la ruta.")
    long_name = models.CharField(
        max_length=255,
        help_text="Nombre largo de la ruta.")
    desc = models.TextField(
        "description",
        blank=True,
        help_text="Descripción detallada de la ruta.")
    route_type = models.IntegerField(
        "route type",
        default=3,
        choices=((0, 'Tranvía o tren ligero.'),
                 (1, 'Subterráneo o metro.'),
                 (2, 'Ferrocarril.'),
                 (3, 'Bus.'),
                 (4, 'Ferry.'),
                 (5, 'Teleférico.'),
                 (6, 'Góndola.'),
                 (7, 'Funicular.')),
        help_text='Medio de transporte usado en la ruta.')
    url = models.CharField(
        max_length=64,
        blank=True, help_text="Página web de la ruta.")
    color = models.CharField(
        max_length=6, blank=True,
        help_text="Color de la ruta en código hexadecimal.")
    text_color = models.CharField(
        max_length=6, blank=True,
        help_text="Color del texto de ruta en código hexadecimal.")

    class Meta:
        verbose_name = "route"
        verbose_name_plural = "routes"

    def __str__(self):
        return self.long_name

class Trip(models.Model):
    """A trip along a route
    This implements trips.txt in the GTFS feed
    """

    objects = tripManager(); # Custom manager with extra methods

    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    service = models.ForeignKey(
        'Calendar', null=True, blank=True, on_delete=models.SET_NULL)
    trip_id = models.CharField(
        primary_key=True,
        max_length=255, db_index=True,
        help_text="Indentificador único de viaje.")
    departure_time = models.TimeField(
        null=True, blank=True,
        help_text="Hora de salida del viaje.")
    arrival_time = models.TimeField(
        null=True, blank=True,
        help_text="Hora de llegada del viaje.")
    headsign = models.CharField(
        max_length=255, blank=True,
        help_text="Identificación de destino para pasajeros.")
    short_name = models.CharField(
        max_length=63, blank=True, null=True,
        help_text="Nombre corto utilizado en horarios y letreros.")
    direction = models.CharField(
        max_length=1, blank=True,
        choices=(('0', 'Hacia San José.'), ('1', 'Desde San José.')),
        help_text="Dirección para rutas en dos sentidos.")
    # block = models.ForeignKey(
    #     'Block', null=True, blank=True, on_delete=models.SET_NULL,
    #     help_text="Block of sequential trips that this trip belongs to.")
    shape = models.ForeignKey(
        'Shape', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="Forma de la ruta.")
    wheelchair_accessible = models.CharField(
        max_length=1, blank=True,
        choices=(
            ('0', 'No hay información.'),
            ('1', 'Hay espacio para el transporte de sillas de ruedas.'),
            ('2', 'No hay espacio para el transporte de sillas de ruedas.')),
        help_text='¿Hay espacio para el transporte de sillas de ruedas?')
    bikes_allowed = models.CharField(
        max_length=1, blank=True,
        choices=(
            ('0', 'No hay información.'),
            ('1', 'Hay espacio para el transporte de bicicletas.'),
            ('2', 'No hay espacio para el transporte de bicicletas.')),
        help_text='¿Hay espacio para el transporte de bicicletas?')

    class Meta:
        verbose_name = "trip"
        verbose_name_plural = "trips"

    def __str__(self):
        return self.trip_id

class StopTime(models.Model):
    """A specific stop on a route on a trip.
    This implements stop_times.txt in the GTFS feed
    """
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    stop = models.ForeignKey('Stop', on_delete=models.CASCADE)
    arrival_time = models.TimeField(
        default=None, null=True, blank=True,
        help_text="Hora de llegada. Debe configurarse para las últimas paradas del viaje.")
    departure_time = models.TimeField(  
        auto_now=False, auto_now_add=False,
        default=None, null=True, blank=True,
        help_text='Hora de salida. Debe configurarse para las últimas paradas del viaje.')
    stop_sequence = models.PositiveIntegerField()
    stop_headsign = models.CharField(
        max_length=255, blank=True,
        help_text="Texto de referencia que identifica la parada para los pasajeros.")
    pickup_type = models.CharField(
        max_length=1, blank=True,
        choices=(('0', 'Recogida programada regularmente.'),
                 ('1', 'No hay recogida disponible.'),
                 ('2', 'Debe llamar a la agencia para coordinar recogida.'),
                 ('3', 'Debe coordinar con conductor para agendar recogida.')),
        help_text="¿Cómo se recoge a los pasajeros?")
    drop_off_type = models.CharField(
        max_length=1, blank=True,
        choices=(('0', 'Llegadas programadas regularmente.'),
                 ('1', 'No hay llegadas disponibles.'),
                 ('2', 'Debe llamar a la agencia para coordinar llegada.'),
                 ('3', 'Debe coordinar con el conductor para agendar la llegada.')),
        help_text="¿Cómo se deja a los pasajeros en su destino?")
    shape_dist_traveled = models.FloatField(
        default=0.0,
        null=True, blank=True,
        help_text='Distance of stop from start of shape')
    timepoint = models.CharField(
        max_length=1, blank=True, default=0,
        choices=(('0', 'Hora aproximada'),
                 ('1', 'Hora exacta')),
        help_text="Exactitud de la hora de llegada y salida.")

    class Meta:
        verbose_name = "stop time"
        verbose_name_plural = "stop times"

    def __str__(self):
        return str(self.trip)

class Calendar(models.Model):
    """Calendar with service disponibility for one or more routes 
    This implements trips.txt in the GTFS feed
    """
    service_id = models.CharField(
        primary_key=True,
        max_length=255, db_index=True,
        help_text="Indentificador único de un calendario.")
    monday = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio sí está disponible los lunes incluidos en este período.'),
            ('0', 'El servcio no está disponible los lunes incluidos en este período.')),
        help_text='¿El servicio está disponible los lunes?')
    tuesday = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio sí está disponible los martes incluidos en este período.'),
            ('0', 'El servcio no está disponible los martes incluidos en este período.')),
        help_text='¿El servicio está disponible los martes?')
    wednesday = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio sí está disponible los miércoles incluidos en este período.'),
            ('0', 'El servcio no está disponible los miércoles incluidos en este período.')),
        help_text='¿El servicio está disponible los miércoles?')    
    thursday = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio sí está disponible los jueves incluidos en este período.'),
            ('0', 'El servcio no está disponible los jueves incluidos en este período.')),
        help_text='¿El servicio está disponible los jueves?')
    friday = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio sí está disponible los viernes incluidos en este período.'),
            ('0', 'El servcio no está disponible los viernes incluidos en este período.')),
        help_text='¿El servicio está disponible los viernes?')
    saturday = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio sí está disponible los sábados incluidos en este período.'),
            ('0', 'El servcio no está disponible los sábados incluidos en este período.')),
        help_text='¿El servicio está disponible los sábados?')
    sunday = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio sí está disponible los domingos incluidos en este período.'),
            ('0', 'El servcio no está disponible los domingos incluidos en este período.')),
        help_text='¿El servicio está disponible los domingos?')
    start_date = models.DateField(
        auto_now=False, auto_now_add=False,
        default=None,
        help_text='Inicio de la vigencia del horario.')
    end_date = models.DateField(
        auto_now=False, auto_now_add=False,
        default=None,
        help_text='Fin de la vigencia del horario.')

    class Meta:
        verbose_name = "calendar"
        verbose_name_plural = "calendars"

    def __str__(self):
        return self.service_id

class CalendarDate(models.Model):
    """Calendar without service disponibility for one or more routes 
    This implements calendar_dates.txt in the GTFS feed
    """
    service = models.ForeignKey('Calendar', on_delete=models.CASCADE)
    date = models.DateField(
        auto_now=False, auto_now_add=False,
        default=None,
        help_text='Fecha en que se aplica el feriado.')
    exception_type = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio ha sido agregado para la fecha especificada.'),
            ('2', 'El servicio ha sido removido de la fecha especificada.')),
        help_text='¿Agregar o remover servicio?')
    holiday_name = models.CharField(
        max_length=64,
        help_text="Nombre oficial del feriado.")

    class Meta:
        verbose_name = "calendar date"
        verbose_name_plural = "calendar dates"

    def __str__(self):
        return f'{self.holiday_name} {self.date.year}'

class FareAttribute(models.Model):
    """A fare attribute class"""

    fare_id = models.CharField(
        primary_key=True,
        max_length=255, db_index=True,
        help_text="Identificador único de la clase de tarifa.")
    price = models.IntegerField(
        help_text="Precio de tarifa, en unidades especificadas en currency_type")
    currency_type = models.CharField(
        max_length=3,
        help_text="Código ISO 4217, alfabético de moneda: CRC.")
    payment_method = models.IntegerField(
        default=1,
        choices=((0, 'La tarifa se paga abordo.'),
                 (1, 'La tarifa se paga previo a subir al transporte.')),
        help_text="¿Cuándo se paga la tarifa?")
    transfers = models.IntegerField(
        default=None, null=True, blank=True,
        choices=((0, 'No se permiten transferencias en esta tarifa.'),
                 (1, 'Los pasajeros pueden transferir una vez.'),
                 (2, 'Los pasajeros pueden transferir dos veces.'),
                 (None, 'Se pueden realizar transferencias ilimitadas.')),
        help_text="¿Se permiten las transferencias?")
    agency = models.ForeignKey('Agency', on_delete=models.CASCADE)
    transfer_duration = models.IntegerField(
        null=True, blank=True,
        help_text="Tiempo en segundos hasta que un tiquete o transferencia expira.")

    class Meta:
        verbose_name = "fare attribute"
        verbose_name_plural = "fare attributes"

    def __str__(self):
        return self.fare_id

class FareRule(models.Model):
    """ A Fare Rule class """

    fare = models.ForeignKey('FareAttribute', on_delete=models.CASCADE)
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    origin = models.ForeignKey('Zone', 
                related_name='origin_id', 
                on_delete=models.CASCADE)
    destination = models.ForeignKey('Zone', 
                related_name='destination_id', 
                on_delete=models.CASCADE)
    class Meta:
        verbose_name = "fare rule"
        verbose_name_plural = "fare rules"

    def __str__(self):
        return self.origin_id + ' > ' + self.destination_id + ' = ' + self.fare_id

class Zone(models.Model):
    """Represents a fare zone.
    This data is not represented as a file in the GTFS. It appears as an
    identifier in the fare_rules and the stops tables.
    """
    zone_id = models.CharField(
        primary_key=True,
        max_length=63, db_index=True,
        help_text="Identificador único de una zona.",
        choices=(('SGAB_A', 'San Gabriel A'),
                 ('SGAB_B', 'San Gabriel B'),
                 ('SGAB_C', 'San Gabriel C'),
                 ('SGAB_D', 'San Gabriel D'),
                 ('ACOS_A', 'Acosta A'),
                 ('ACOS_B', 'Acosta B'),
                 ('ACOS_C', 'Acosta C'),
                 ('ACOS_D', 'Acosta D'),
                 ('RUTA_E', 'Ruta E'),
                 ('RUTA_F', 'Ruta F'),
                 ('RUTA_G', 'Ruta G'),),
        )

    class Meta:
        verbose_name = "zone"
        verbose_name_plural = "zones"

    def __str__(self):
        return self.zone_id

# class Shape(models.Model):
#     """The path the vehicle takes along the route.
#     Implements shapes.txt."""
#     shape_id = models.CharField(
#         max_length=255, db_index=True,
#         help_text="Unique identifier for a shape.")
#     geometry = models.LineStringField(
#         null=True, blank=True,
#         help_text='Geometry cache of ShapePoints')

class Shape(models.Model):
    """The path the vehicle takes along the route.
    Implements shapes.txt."""
    shape_id = models.CharField(
        primary_key=True,
        max_length=255, db_index=True,
        help_text="Identificador único de una trayectoria.")
    pt_lat = models.DecimalField(
        max_digits=22,
        decimal_places=16,
        help_text='Latitud WGS 84 de punto de la trayectoria.')
    pt_lon = models.DecimalField(
        max_digits=22,
        decimal_places=16,
        help_text='Longitud WGS 84 de punto de la trayectoria.')
    pt_sequence = models.PositiveIntegerField(
        help_text='Secuencia en la que los puntos de la trayectoria se conectan para crear la forma')
    dist_traveled = models.DecimalField(default=0.0,
        max_digits=6,
        decimal_places=3, 
        null=True, blank=True,
        help_text="Precisión es en metros (0.001 km)")

    class Meta:
        verbose_name = "shape"
        verbose_name_plural = "shapes"

    def __str__(self):
        return self.shape_id

class FeedInfo(models.Model):
    """ Información sobre los que hacen el GTFS """

    publisher_name = models.CharField(max_length=128,
        help_text="Quiénes hicieron el GTFS.")
    publisher_url = models.URLField(
        blank=True, help_text="URL de los que hicieron el GTFS.")
    lang = models.CharField(
        max_length=2, blank=True,
        help_text="Código ISO 639-1 de idioma del suministro.")
    start_date = models.DateField(
        blank=True, null=True,
        help_text='Fecha en inicia la validez del suministro GTFS.')
    end_date = models.DateField(
        blank=True, null=True,
        help_text='Fecha en termina la validez del suministro GTFS.')
    version = models.CharField(max_length=32)
    contact_email = models.EmailField(max_length=128,  
        blank=True, help_text="Correo electrónico de contacto sobre GTFS.")
    
    class Meta:
        verbose_name = "feed info"
        verbose_name_plural = "feed info objects"

    def __str__(self):
        return self.publisher_name


class Fecha(models.Model):
    """ Fechas de modificación de horarios o tarifas """
    titulo = models.CharField(max_length=255)
    horarios = models.CharField(max_length=127, blank=True, null=True)
    tarifas = models.CharField(max_length=127, blank=True, null=True)
    ruta = models.ManyToManyField('Route')

    def __str__(self):
        return self.titulo
    

class Anuncio(models.Model):
    """ Anuncios de la agencia """
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    ruta = models.ManyToManyField('Route')
    fecha_modificacion = models.DateField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.titulo