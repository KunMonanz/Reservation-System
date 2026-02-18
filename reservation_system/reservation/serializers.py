from .models import Table, Reservation

from rest_framework.serializers import (
    ModelSerializer,
    ValidationError
)


class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'number', 'seat', 'location']
        read_only_fields = ['id']

        def validate(self, data):
            seat = data.get('seat')
            if seat == 0:
                raise ValidationError(
                    "Seat count must be greater than zero."
                )
            return data


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'id',
            'table',
            'user',
            'date',
            'time',
            'guests',
            'created_at'
        ]
        read_only_fields = ['id', 'user', 'created_at']

        def validate(self, data):
            table = data.get('table')
            guests = data.get('guests')

            if guests == 0:
                raise ValidationError(
                    "Guest count must be greater than zero."
                )
            if guests > table.seat:
                raise ValidationError(
                    f"Guest count cannot exceed table seat count of {table.seat}."
                )
            return data
