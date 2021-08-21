from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.nuevo),
    path('shows/<int:id>/edit', views.editar),
    path('shows/<int:id>', views.mostrar),
    path('shows/<int:id>/delete', views.borrar),
    path('shows/crear_show/', views.crear_show),
    path('shows/actualizar_show/<int:id>', views.actualizar_show),
]