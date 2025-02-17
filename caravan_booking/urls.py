"""
URL configuration for caravan_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.contrib import admin


# Language switcher (remains outside)
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# Include all other URLs with language prefix
urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('user_settings/', include('user_settings.urls')),
)
