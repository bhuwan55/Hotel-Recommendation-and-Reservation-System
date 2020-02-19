from django.urls import path
from . import views
app_name='reserve'

urlpatterns = [

    path('details/<int:id>/reserve/',views.reserve,name='reserve'),


]
