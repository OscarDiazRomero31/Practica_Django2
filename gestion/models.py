from django.db import models
from django.contrib.auth.models import User

class Coche(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano_fabricacion = models.DateField()

    def __str__(self):
        return f"{self.marca} {self.nombre}"

class Empleado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class ServicioMantenimiento(models.Model):
    descripcion = models.TextField()
    fecha_servicio = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descripcion

class Venta(models.Model):
    coche = models.ForeignKey(Coche, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta = models.DateField()

    def __str__(self):
        return f"Venta de {self.coche} a {self.cliente}"
