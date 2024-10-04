from django.shortcuts import render
from .models import Coche, Empleado, Cliente, ServicioMantenimiento, Venta

def listar_coches(request):
    coches = Coche.objects.all()
    return render(request, 'coches.html', {'coches': coches})

def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados.html', {'empleados': empleados})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def listar_servicios(request):
    servicios = ServicioMantenimiento.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})

def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas.html', {'ventas': ventas})
