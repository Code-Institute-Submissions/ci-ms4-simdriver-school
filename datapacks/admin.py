from django.contrib import admin
from .models import Week, Datapack, RaceTrack

# Register your models here.


class WeekAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('id',)


class RaceTrackAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('name',)


class DatapackAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'week',
        'track_name'
    )

    ordering = ('product', 'week',)

admin.site.register(Week, WeekAdmin)
admin.site.register(Datapack, DatapackAdmin)
admin.site.register(RaceTrack, RaceTrackAdmin)