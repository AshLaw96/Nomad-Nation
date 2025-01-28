from django.urls import path
from . import views


urlpatterns = [
    path('listings/', views.listings_view, name='listings'),
