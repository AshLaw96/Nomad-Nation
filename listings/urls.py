from django.urls import path
from . import views


urlpatterns = [
    path('listings/', views.listings_view, name='listings'),
    path('add/', views.add_caravan, name='add_caravan'),
