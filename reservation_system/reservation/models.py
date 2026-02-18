from django.db import models
from django.conf import settings


class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    seat = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f'Table {self.number} - {self.seat} seats - {self.location}'


class Reservation(models.Model):
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name='reservations'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reservations'
    )
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('table', 'date', 'time')

    def __str__(self):
        return f'Reservation for {self.user.username} at Table {self.table.number} on {self.date} at {self.time}'
