from django.contrib import admin
from django.urls import path
from teams import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('drivers/', views.drivers, name='drivers'),
    path('races/', views.races, name='races'),
    path('results/', views.results, name='results'),
]
