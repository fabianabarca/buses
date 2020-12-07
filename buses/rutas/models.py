from django.db import models

# from django.contrib.gis.geos import LineString

""" 
Clases a crear 
    - Agencia (agency)
    - Paradas (stops)
    - Rutas (routes)
    - Viajes (trips)
    - Horario (stop_times)
    - Calendario (calendar)
    - Feriados (calendar_dates)
    *****
    *****
    - Zone  Para agregar tarifas - ForeignKey en Stop
    - Fare  Para agregar tarifas
    - Shape Se usa como ForeignKey en Trip

Nota: todos deben tener el __str__()
"""
class Agency(models.Model):
    """One or more transit agencies that provide the data in this feed.
    Maps to agency.txt in the GTFS feed.
    """
    agency_id = models.CharField(
        primary_key=True,
        max_length=255, blank=True, db_index=True,
        help_text="Unique identifier for transit agency")
    name = models.CharField(
        max_length=255,
        help_text="Full name of the transit agency")
    url = models.URLField(
        blank=True, help_text="URL of the transit agency")
    timezone = models.CharField(
        max_length=255,
        help_text="Timezone of the agency")
    lang = models.CharField(
        max_length=2, blank=True,
        help_text="ISO 639-1 code for the primary language")
    phone = models.CharField(
        max_length=255, blank=True,
        help_text="Voice telephone number")
    fare_url = models.URLField(
        blank=True, help_text="URL for purchasing tickets online")
    email = models.EmailField(max_length=254,  blank=True, help_text="Customer Service email")

    def __str__(self):
        return self.name

class Stop(models.Model):
    """A stop or station
    Maps to stops.txt in the GTFS feed.
    """    
    stop_id = models.CharField(
        primary_key=True,
        max_length=255, db_index=True,
        help_text="Unique identifier for a stop or station.")
    code = models.CharField(
        max_length=255, blank=True,
        help_text="Uniquer identifier (short text or number) for passengers.")
    name = models.CharField(
        max_length=255,
        help_text="Name of stop in local vernacular.")
    # tts_stop_name = models.CharField(
    #     max_length=255,
    #     help_text="Readable version of the name (no abbreviations).")
    desc = models.CharField(
        "description",
        max_length=255, blank=True,
        help_text='Description of a stop.')
    lat = models.DecimalField(
        max_digits=22,
        decimal_places=16,
        help_text='WGS 84 latitude of stop or station')
    lon = models.DecimalField(
        max_digits=22,
        decimal_places=16,
        help_text='WGS 84 longitude of stop or station')
    zone = models.ForeignKey(
        'Zone', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="Fare zone for a stop ID.")
    url = models.URLField(
        blank=True, help_text="URL for the stop")
    location_type = models.CharField(
        max_length=1, blank=True, choices=(('0', 'Stop'), ('1', 'Station')),
        help_text="Is this a stop or station?")
    parent_station = models.ForeignKey(
        'Stop', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="The station associated with the stop")
    timezone = models.CharField(
        max_length=255, blank=True,
        help_text="Timezone of the stop")
    wheelchair_boarding = models.CharField(
        max_length=1, blank=True,
        choices=(
            ('0', 'No information'),
            ('1', 'Some wheelchair boarding'),
            ('2', 'No wheelchair boarding')),
        help_text='Is wheelchair boarding possible?')
    
    def __str__(self):
        return self.stop_id

class Route(models.Model):
    """A transit route
    Maps to route.txt in the GTFS feed.
    """
    route_id = models.CharField(
        primary_key=True,
        max_length=64, db_index=True,
        help_text="Unique identifier for route.")
    agency = models.ForeignKey(
        'Agency', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="Agency for this route.")
    short_name = models.CharField(
        max_length=63,
        help_text="Short name of the route")
    long_name = models.CharField(
        max_length=255,
        help_text="Long name of the route")
    desc = models.TextField(
        "description",
        blank=True,
        help_text="Long description of a route")
    route_type = models.IntegerField(
        "route type",
        default=3,
        choices=((0, 'Tram, Streetcar, or Light rail'),
                 (1, 'Subway or Metro'),
                 (2, 'Rail'),
                 (3, 'Bus'),
                 (4, 'Ferry'),
                 (5, 'Cable car'),
                 (6, 'Gondola or Suspended cable car'),
                 (7, 'Funicular')),
        help_text='Type of transportation used on route')
    url = models.CharField(
        max_length=32,
        blank=True, help_text="Web page about for the route")
    color = models.CharField(
        max_length=6, blank=True,
        help_text="Color of route in hex")
    text_color = models.CharField(
        max_length=6, blank=True,
        help_text="Color of route text in hex")
    
    def __str__(self):
        return self.long_name

class Trip(models.Model):
    """A trip along a route
    This implements trips.txt in the GTFS feed
    """
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    service = models.ForeignKey(
        'Calendar', null=True, blank=True, on_delete=models.SET_NULL)
    trip_id = models.CharField(
        primary_key=True,
        max_length=255, db_index=True,
        help_text="Unique identifier for a trip.")
    headsign = models.CharField(
        max_length=255, blank=True,
        help_text="Destination identification for passengers.")
    short_name = models.CharField(
        max_length=63, blank=True,
        help_text="Short name used in schedules and signboards.")
    direction = models.CharField(
        max_length=1, blank=True,
        choices=(('0', 'Hacia San José'), ('1', 'Desde San José')),
        help_text="Dirección para rutas en dos sentidos.")
    # block = models.ForeignKey(
    #     'Block', null=True, blank=True, on_delete=models.SET_NULL,
    #     help_text="Block of sequential trips that this trip belongs to.")
    shape = models.ForeignKey(
        'Shape', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="Shape used for this trip")
    wheelchair_accessible = models.CharField(
        max_length=1, blank=True,
        choices=(
            ('0', 'No information'),
            ('1', 'Some wheelchair accommodation'),
            ('2', 'No wheelchair accommodation')),
        help_text='Are there accommodations for riders with wheelchair?')
    bikes_allowed = models.CharField(
        max_length=1, blank=True,
        choices=(
            ('0', 'No information'),
            ('1', 'Some bicycle accommodation'),
            ('2', 'No bicycles allowed')),
        help_text='Are bicycles allowed?')
    
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
        help_text="Arrival time. Must be set for end stops of trip.")
    departure_time = models.TimeField(  
        auto_now=False, auto_now_add=False,
        default=None, null=True, blank=True,
        help_text='Departure time. Must be set for end stops of trip.')
    stop_sequence = models.PositiveIntegerField()
    stop_headsign = models.CharField(
        max_length=255, blank=True,
        help_text="Sign text that identifies the stop for passengers")
    pickup_type = models.CharField(
        max_length=1, blank=True,
        choices=(('0', 'Regularly scheduled pickup'),
                 ('1', 'No pickup available'),
                 ('2', 'Must phone agency to arrange pickup'),
                 ('3', 'Must coordinate with driver to arrange pickup')),
        help_text="How passengers are picked up")
    drop_off_type = models.CharField(
        max_length=1, blank=True,
        choices=(('0', 'Regularly scheduled drop off'),
                 ('1', 'No drop off available'),
                 ('2', 'Must phone agency to arrange drop off'),
                 ('3', 'Must coordinate with driver to arrange drop off')),
        help_text="How passengers are picked up")
    # shape_dist_traveled = models.FloatField(
    #     "shape distance traveled",
    #     null=True, blank=True,
    #     help_text='Distance of stop from start of shape')
    # timepoint = models.CharField(
    #     max_length=1, blank=True, default=0,
    #     choices=(('0', 'Hora aproximada'),
    #              ('1', 'Hora exacta')),
    #     help_text="Exactitud de la hora de llegada y salida")
    
    def __str__(self):
        return str(self.trip)

class Calendar(models.Model):
    """Calendar with service disponibility for one or more routes 
    This implements trips.txt in the GTFS feed
    """
    service_id = models.CharField(
        primary_key=True,
        max_length=255, db_index=True,
        help_text="Unique identifier for a service calendar.")
    monday = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio sí está disponible los lunes incluidos en este período'),
            ('0', 'El servcio no está disponible los lunes incluidos en este período')),
        help_text='¿El servicio está disponible los lunes?')
    tuesday = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio sí está disponible los martes incluidos en este período'),
            ('0', 'El servcio no está disponible los martes incluidos en este período')),
        help_text='¿El servicio está disponible los martes?')
    wednesday = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio sí está disponible los miércoles incluidos en este período'),
            ('0', 'El servcio no está disponible los miércoles incluidos en este período')),
        help_text='¿El servicio está disponible los miércoles?')    
    thursday = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio sí está disponible los jueves incluidos en este período'),
            ('0', 'El servcio no está disponible los jueves incluidos en este período')),
        help_text='¿El servicio está disponible los jueves?')
    friday = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio sí está disponible los viernes incluidos en este período'),
            ('0', 'El servcio no está disponible los viernes incluidos en este período')),
        help_text='¿El servicio está disponible los viernes?')
    saturday = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio sí está disponible los sábados incluidos en este período'),
            ('0', 'El servcio no está disponible los sábados incluidos en este período')),
        help_text='¿El servicio está disponible los sábados?')
    sunday = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio sí está disponible los domingos incluidos en este período'),
            ('0', 'El servcio no está disponible los domingos incluidos en este período')),
        help_text='¿El servicio está disponible los domingos?')
    start_date = models.DateField(
        auto_now=False, auto_now_add=False,
        default=None,
        help_text='Inicio de la vigencia del horario')
    end_date = models.DateField(
        auto_now=False, auto_now_add=False,
        default=None,
        help_text='Fin de la vigencia del horario')
    
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
        help_text='Fecha en que se aplica el feriado')
    exception_type = models.CharField(
        max_length=1,
        choices=(
            ('1', 'El servicio ha sido agregado para la fecha especificada'),
            ('2', 'El servicio ha sido removido de la fecha especificada')),
        help_text='¿Agregar o remover servicio?')
    holiday_name = models.CharField(
        max_length=64,
        help_text="Nombre oficial del feriado")

    def __str__(self):
        return self.holiday_name

class Fare(models.Model):
    """A fare class"""

    fare_id = models.CharField(
        primary_key=True,
        max_length=255, db_index=True,
        help_text="Unique identifier for a fare class")
    price = models.DecimalField(
        max_digits=17, decimal_places=4,
        help_text="Fare price, in units specified by currency_type")
    currency_type = models.CharField(
        max_length=3,
        help_text="ISO 4217 alphabetical currency code: CRC")
    payment_method = models.IntegerField(
        default=1,
        choices=((0, 'Fare is paid on board.'),
                 (1, 'Fare must be paid before boarding.')),
        help_text="When is the fare paid?")
    transfers = models.IntegerField(
        default=None, null=True, blank=True,
        choices=((0, 'No transfers permitted on this fare.'),
                 (1, 'Passenger may transfer once.'),
                 (2, 'Passenger may transfer twice.'),
                 (None, 'Unlimited transfers are permitted.')),
        help_text="Are transfers permitted?")
    transfer_duration = models.IntegerField(
        null=True, blank=True,
        help_text="Time in seconds until a ticket or transfer expires")

    def __str__(self):
        return self.fare_id

class Zone(models.Model):
    """Represents a fare zone.
    This data is not represented as a file in the GTFS. It appears as an
    identifier in the fare_rules and the stop tables.
    """
    zone_id = models.CharField(
        primary_key=True,
        max_length=63, db_index=True,
        help_text="Unique identifier for a zone.")

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
        help_text="Unique identifier for a shape.")
    pt_lat = models.DecimalField(
        max_digits=22,
        decimal_places=16,
        help_text='WGS 84 latitude of point of shape')
    pt_lon = models.DecimalField(
        max_digits=22,
        decimal_places=16,
        help_text='WGS 84 longitude of point of shape')
    pt_sequence = models.PositiveIntegerField(
        help_text='Sequence in which the shape points connect to form the shape')
    
    def __str__(self):
        return self.shape_id