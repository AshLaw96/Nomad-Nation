from django.urls import path
from . import views


urlpatterns = [
    path('account_settings/', views.account_settings, name='account_settings'),
]
