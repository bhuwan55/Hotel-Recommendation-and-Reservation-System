from django.urls import path,include
from . import views
from django.contrib.auth.views  import LoginView, LogoutView
app_name='user'

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='user:login'),name='logout'),
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
]
