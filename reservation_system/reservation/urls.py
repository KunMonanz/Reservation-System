from django.urls import path

from .views import (
    AvailableTablesView,
    ReservationListCreateView,
    TableListCreateView
)

urlpatterns = [
    path(
        'v1/tables/',
        TableListCreateView.as_view(),
        name='table-list-create'
    ),
    path(
        'v1/reservations/',
        ReservationListCreateView.as_view(), name='reservation-list-create'
    ),
    path(
        'v1/available-tables/',
        AvailableTablesView.as_view(),
        name='available-table-list'
    )
]
