from django.contrib import admin
from .models import Coche, Empleado, Cliente, ServicioMantenimiento, Venta

admin.site.register(Coche)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(ServicioMantenimiento)
admin.site.register(Venta)
