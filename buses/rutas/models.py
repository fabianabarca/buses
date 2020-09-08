from django.db import models

# from django.contrib.gis.geos import LineString

""" 
Clases a crear 
    - Agencia
    - Parada
    - Ruta
    - Viaje
    - Horario
    - Calendario
    - Feriado
    *****
    *****
    - Zone  Para agregar tarifas - ForeignKey en Stop
    - Fare  Para agregar tarifas
    - Shape Se usa como ForeignKey en Trip
"""
class Agency(models.Model):
    """One or more transit agencies that provide the data in this feed.
    Maps to agency.txt in the GTFS feed.
    """
    agency_id = models.CharField(
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

class Stop(models.Model):
    """A stop or station
    Maps to stops.txt in the GTFS feed.
    """    
    stop_id = models.CharField(
        max_length=255, db_index=True,
        help_text="Unique identifier for a stop or station.")
    code = models.CharField(
        max_length=255, blank=True,
        help_text="Uniquer identifier (short text or number) for passengers.")
    name = models.CharField(
        max_length=255,
        help_text="Name of stop in local vernacular.")
    desc = models.CharField(
        "description",
        max_length=255, blank=True,
        help_text='Description of a stop.')
    stop_lat = models.DecimalField(
        max_digits=22,
        decimal_places=16,
        help_text='WGS 84 latitude of stop or station')
    stop_lon = models.DecimalField(
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

class Route(models.Model):
    """A transit route
    Maps to route.txt in the GTFS feed.
    """

    route_id = models.CharField(
        max_length=255, db_index=True,
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
    rtype = models.IntegerField(
        "route type",
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

class Trip(models.Model):
    """A trip along a route
    This implements trips.txt in the GTFS feed
    """
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    # service = models.ForeignKey(
    #     'Service', null=True, blank=True, on_delete=models.SET_NULL)
    trip_id = models.CharField(
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
        choices=(('0', '0'), ('1', '1')),
        help_text="Direction for bi-directional routes.")
    # block = models.ForeignKey(
    #     'Block', null=True, blank=True, on_delete=models.SET_NULL,
    #     help_text="Block of sequential trips that this trip belongs to.")
    # shape = models.ForeignKey(
    #     'Shape', null=True, blank=True, on_delete=models.SET_NULL,
    #     help_text="Shape used for this trip")
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
    stop_sequence = models.IntegerField()
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
    shape_dist_traveled = models.FloatField(
        "shape distance traveled",
        null=True, blank=True,
        help_text='Distance of stop from start of shape')

class Calendar(models.Model):
    """Calendar with service disponibility for one or more routes 
    This implements trips.txt in the GTFS feed
    """
    service_id = models.CharField(
        max_length=255, db_index=True,
        help_text="Unique identifier for a service calendar.")
    monday = models.CharField(
        max_length=1,
        choices=(
            ('0', 'The service is available on mondays included in this period'),
            ('1', 'The service is not available on mondays included in this period')),
        help_text='Is the service available on mondays?')
    tuesday = models.CharField(
        max_length=1,
        choices=(
            ('0', 'The service is available on tuesdays included in this period'),
            ('1', 'The service is not available on tuesdays included in this period')),
        help_text='Is the service available on tuesdays?')
    wednesday = models.CharField(
        max_length=1,
        choices=(
            ('0', 'The service is available on wednesdays included in this period'),
            ('1', 'The service is not available on wednesdays included in this period')),
        help_text='Is the service available on wednesdays?')    
    thursday = models.CharField(
        max_length=1,
        choices=(
            ('0', 'The service is available on thursdays included in this period'),
            ('1', 'The service is not available on thursdays included in this period')),
        help_text='Is the service available on thursdays?')
    friday = models.CharField(
        max_length=1,
        choices=(
            ('0', 'The service is available on fridays included in this period'),
            ('1', 'The service is not available on fridays included in this period')),
        help_text='Is the service available on fridays?')
    saturday = models.CharField(
        max_length=1,
        choices=(
            ('0', 'The service is available on saturdays included in this period'),
            ('1', 'The service is not available on saturdays included in this period')),
        help_text='Is the service available on saturdays?')
    sunday = models.CharField(
        max_length=1,
        choices=(
            ('0', 'The service is available on sundays included in this period'),
            ('1', 'The service is not available on sundays included in this period')),
        help_text='Is the service available on sundays?')
    start_date = models.DateField(
        auto_now=False, auto_now_add=False,
        default=None,
        help_text='Service start date')
    end_date = models.DateField(
        auto_now=False, auto_now_add=False,
        default=None,
        help_text='Service start date')

class CalendarDates(models.Model):
    """Calendar without service disponibility for one or more routes 
    This implements trips.txt in the GTFS feed
    """
    service_id = models.ForeignKey('Calendar', on_delete=models.CASCADE)
    date = models.DateField(
        auto_now=False, auto_now_add=False,
        default=None,
        help_text='Service exception date')

class Fare(models.Model):
    """A fare class"""

    fare_id = models.CharField(
        max_length=255, db_index=True,
        help_text="Unique identifier for a fare class")
    price = models.DecimalField(
        max_digits=17, decimal_places=4,
        help_text="Fare price, in units specified by currency_type")
    currency_type = models.CharField(
        max_length=3,
        help_text="ISO 4217 alphabetical currency code")
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

class Zone(models.Model):
    """Represents a fare zone.
    This data is not represented as a file in the GTFS.  It appears as an
    identifier in the fare_rules and the stop tables.
    """
    zone_id = models.CharField(
        max_length=63, db_index=True,
        help_text="Unique identifier for a zone.")

# class Shape(models.Model):
#     """The path the vehicle takes along the route.
#     Implements shapes.txt."""
#     shape_id = models.CharField(
#         max_length=255, db_index=True,
#         help_text="Unique identifier for a shape.")
#     geometry = models.LineStringField(
#         null=True, blank=True,
#         help_text='Geometry cache of ShapePoints')

