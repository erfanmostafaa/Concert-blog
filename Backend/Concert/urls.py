"""
URL configuration for Concert project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin # type: ignore
from django.urls import path          # type: ignore
from django.conf import settings    # type: ignore
from django.conf.urls.static import static  # type: ignore
from Ticketsales.views import ConcertListView , LocationView , TimeView , Concertdetail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Ticketsales/Concert/list',ConcertListView),
    path('Ticketsales/location/list',LocationView),
    path('Ticketsales/time/list',TimeView),
    path('Ticketsales/Concert/<int:concert_id>', Concertdetail)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)