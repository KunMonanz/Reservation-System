from django_filters import rest_framework as filters

from .models import Table


class TableFilter(filters.FilterSet):
    location = filters.CharFilter(
        field_name='location',
        lookup_expr='icontains'
    )
    max_seat = filters.NumberFilter(
        field_name='seat',
        lookup_expr='lte'
    )
    min_seat = filters.NumberFilter(
        field_name='seat',
        lookup_expr='gte'
    )

    class Meta:
        model = Table
        fields = ['location', 'seat']
