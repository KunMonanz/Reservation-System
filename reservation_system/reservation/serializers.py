from .models import Table, Reservation
from rest_framework.serializers import ModelSerializer


class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'number', 'seat', 'location']
        read_only_fields = ['id']


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
