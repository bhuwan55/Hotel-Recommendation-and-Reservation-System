from django.urls import include, path
from . import views

app_name='all_hotels'

urlpatterns = [
path('<int:id>/',views.category_hotel,name='category_hotel'),
path('details/<int:id>/',views.hotel,name='hotel'),
path('details/<int:id>/rate/',views.rate,name='rate'),
path('detailhotel/<int:id>/',views.detailhotel,name='detailhotel'),
path('details/<int:id>/reserve/',views.reserve,name='reserve'),

]
