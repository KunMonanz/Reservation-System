import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.forms import ValidationError
from django.core.validators import MinValueValidator


class Table(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    number = models.PositiveIntegerField(unique=True)
    seat = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    location = models.CharField(max_length=100)

    def clean(self):
        if self.seat == 0:
            raise ValidationError(
                "Seat count must be greater than zero."
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Table {self.number} - {self.seat} seats - {self.location}'


class Reservation(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED = 'cancelled', 'Cancelled'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
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
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('table', 'date', 'time')

    def clean(self):
        if self.guests == 0:
            raise ValidationError(
                "Guest count must be greater than zero."
            )
        if self.guests > self.table.seat:
            raise ValidationError(
                f"Guest count cannot exceed table seat count of {self.table.seat}."
            )
        if self.date < timezone.now().date():
            raise ValidationError("Cannot reserve in the past.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Reservation for {self.user.username} at Table {self.table.number} on {self.date} at {self.time}'
