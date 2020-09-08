from django.contrib import admin
from rutas.models import Agency, Stop, Route, Trip, StopTime, Calendar, CalendarDates, Fare, Zone

admin.site.register(Agency)
admin.site.register(Stop)
admin.site.register(Route)
admin.site.register(Trip)
admin.site.register(StopTime)
admin.site.register(Calendar)
admin.site.register(CalendarDates)
admin.site.register(Fare)
admin.site.register(Zone)
