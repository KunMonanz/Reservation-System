from django.contrib import admin

from django.contrib import admin
from .models import Table, Reservation


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seat', 'location')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'date', 'time')
    list_filter = ('date',)

    def user(self, reservation: Reservation):
        return reservation.user.username
