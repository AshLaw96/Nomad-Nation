from django.urls import path
from . import views


urlpatterns = [
    path('account_settings/', views.account_settings, name='account_settings'),
    path(
        'edit_personal_details/',
        views.edit_personal_details,
        name='edit_personal_details'
    ),
    path('edit_preferences/', views.edit_preferences, name='edit_preferences'),
    path(
        'edit_payment_details/',
        views.edit_payment_details,
        name='edit_payment_details'
    ),
    path(
        'edit_privacy_settings/',
        views.edit_privacy_settings,
        name='edit_privacy_settings'
    ),
    path(
        'convert_currency/',
        views.convert_currency_view,
        name='convert_currency'
    ),
]
