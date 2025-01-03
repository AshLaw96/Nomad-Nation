from django.urls import path
from . import views, auth_views


print("Register view:", auth_views.register)
urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('signup/', auth_views.register, name='custom_account_signup'),
]
