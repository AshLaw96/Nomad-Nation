from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact/', views.contact_view, name='contact'),
    path(
        'contact/delete/<int:message_id>/',
        views.delete_message,
        name='delete_message'
    ),
]
