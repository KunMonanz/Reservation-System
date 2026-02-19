from .models import Table, Reservation

from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    StringRelatedField
)


class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'number', 'seat', 'location']
        read_only_fields = ['id']

    def validate(self, attrs):
        seat = attrs.get('seat')
        if seat == 0:
            raise ValidationError(
                "Seat count must be greater than zero."
            )
        return attrs


class ReservationSerializer(ModelSerializer):
    username = StringRelatedField(read_only=True, source='user.username')

    class Meta:
        model = Reservation
        fields = [
            'id',
            'table',
            'user',
            'username',
            'date',
            'time',
            'guests',
            'status',
            'created_at'
        ]
        read_only_fields = [
            'id',
            'user',
            'created_at',
            'status',
            'username'
        ]

    def validate(self, attrs):
        table = attrs.get('table')
        guests = attrs.get('guests')

        if guests == 0:
            raise ValidationError(
                "Guest count must be greater than zero."
            )
        if guests > table.seat:
            raise ValidationError(
                f"Guest count cannot exceed table seat count of {table.seat}."
            )
        return attrs
