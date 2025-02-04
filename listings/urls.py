from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.listings_view, name='listings'),
    path('add/', views.add_caravan, name='add_caravan'),
    path('edit/<int:pk>/', views.edit_caravan, name='edit_caravan'),
    path('delete/<int:pk>/', views.delete_caravan, name='delete_caravan'),
    path('bookings/', views.booking_page_view, name='booking_page'),
    path('booking/<int:caravan_id>/', views.book_caravan, name='book_caravan'),
    path(
        'bookings/<int:caravan_id>/',
        views.booking_view,
        name='booking_view'
    ),
    path(
        'manage_booking/<int:booking_id>/',
        views.manage_booking,
        name='manage_booking'
    ),
    path(
        'modify_booking/<int:booking_id>/',
        views.modify_booking,
        name='modify_booking'
    )
]
