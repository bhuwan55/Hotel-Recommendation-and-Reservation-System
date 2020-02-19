from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views

urlpatterns = [
    path('home/',views.index,name='home'),  
    path('admin/', admin.site.urls),
    path('hotel/',include('all_hotels.urls', namespace='all_hotels')),
    path('user/',include('user.urls',namespace='user')),
    path('contact/',include('contact.urls', namespace='contact')),
    path('team/',views.team,name='team'),
    path('search/',views.search,name='search'),
    path('searchloc/',views.searchloc,name='searchloc'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
