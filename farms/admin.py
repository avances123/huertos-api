from django.contrib import admin
from farms.models import Farm,Zone

class ZoneAdmin(admin.StackedInline):
    model = Zone

class FarmAdmin(admin.ModelAdmin):
    inlines = [ZoneAdmin]


admin.site.register(Farm,FarmAdmin)
admin.site.register(Zone)

