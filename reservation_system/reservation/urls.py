from django.urls import path

from .views import (
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
]
