from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly
)

from django_filters.rest_framework import DjangoFilterBackend

from .filters import TableFilter

from .models import Reservation, Table

from .serializers import (
    TableSerializer,
    ReservationSerializer
)


class TableListCreateView(ListCreateAPIView):
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TableFilter

    def get_queryset(self):
        return Table.objects.all()


class ReservationListCreateView(ListCreateAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects \
            .select_related('table') \
            .filter(user=self.request.user, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        table = serializer.validated_data['table']
        table.is_reserved = True
        table.save()


class AvailableTablesView(ListCreateAPIView):
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Table.objects.filter(is_reserved=False)
