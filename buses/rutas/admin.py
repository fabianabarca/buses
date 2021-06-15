from django.contrib import admin
from rutas.models import Agency, Stop, Route, Trip, StopTime, Calendar, CalendarDate, FareAttribute, FareRule, Zone, Shape, FeedInfo

admin.site.register(Agency)
admin.site.register(Stop)
admin.site.register(Route)
admin.site.register(Trip)
admin.site.register(StopTime)
admin.site.register(Calendar)
admin.site.register(CalendarDate)
admin.site.register(FareAttribute)
admin.site.register(FareRule)
admin.site.register(Zone)
admin.site.register(Shape)
admin.site.register(FeedInfo)
