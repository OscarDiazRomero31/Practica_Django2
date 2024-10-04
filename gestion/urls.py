from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_coches, name='listar_coches'),
    path('empleados/', views.listar_empleados, name='listar_empleados'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('servicios/', views.listar_servicios, name='listar_servicios'),
    path('ventas/', views.listar_ventas, name='listar_ventas'),
]
