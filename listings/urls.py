from django.urls import path
from . import views


urlpatterns = [
    path('listings/', views.listings_view, name='listings'),
    path('add/', views.add_caravan, name='add_caravan'),
    path('edit/<int:pk>/', views.edit_caravan, name='edit_caravan'),
    path('delete/<int:pk>/', views.delete_caravan, name='delete_caravan'),
    path('booking/<int:caravan_id>/', views.booking_view, name='book_caravan'),
    path('bookings/', views.bookings_view, name='bookings'),
]
