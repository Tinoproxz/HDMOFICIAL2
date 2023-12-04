from decimal import Decimal
from django.db import models
from django.core import validators



# Create your models here.
class Usuario(models.Model):
    ESTADOS=[('activo', 'Habilitado'),('inactivo', 'Deshabilitado'),]
    CARGO=[('administrador', 'Administrador'),('encargado', 'Encargado'),]

    rut_usu = models.CharField(primary_key=True,verbose_name="Rut",max_length=12,validators=[validators.MinLengthValidator(9), validators.MaxLengthValidator(12)])
    nombre = models.CharField(max_length=80,validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(80)])
    apellidos = models.CharField(max_length=80,validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(80)])
    cargo = models.CharField(max_length=15,choices=CARGO)
    password = models.CharField(max_length=30)
    estado = models.CharField(max_length=15,choices=ESTADOS)

    def __str__(self):
        return self.rut_usu

class Habitaciones(models.Model):
    ESTADOS=[('disponible', 'Disponible'),('no disponible', 'No Disponible'),('mantencion','En Mantencion'),]
    ORIENTACION=[('norte', 'Norte'),('sur', 'Sur'),('este','Este'),('oeste','Oeste'),]
    PRECIO=[('25.000', '$25.000'),('40.000', '$40.000'),('75.000','$75.000')]
    CAPACIDAD=[('2', '2 Personas'),('4', '4 Personas'),('6','6 Personas')]

    num_habi = models.IntegerField(primary_key=True,verbose_name="Numero Habitacion")
    estado = models.CharField(max_length=30,choices=ESTADOS)
    orientacion = models.CharField(max_length=30,choices=ORIENTACION)
    prec_habi = models.CharField(max_length=30,choices=PRECIO,verbose_name="Precio")
    capacidad = models.CharField(max_length=30,choices=CAPACIDAD)

    def __str__(self):
        return str(self.num_habi) + ' ( Capacidad: ' + self.capacidad + ' /  Estado: '+ self.estado +' ) '
        

class Huespedes(models.Model):
    rut = models.CharField(primary_key=True,max_length=12,validators=[validators.MinLengthValidator(8), validators.MaxLengthValidator(12)])
    nombre = models.CharField(max_length=80,validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(80)])
    apellidos = models.CharField(max_length=80,validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(80)])
    correo = models.EmailField()
    num_telefono = models.CharField(max_length=12,validators=[validators.MaxLengthValidator(12), validators.MinLengthValidator(9)],verbose_name="Numero Telefono")
    residencia = models.CharField(max_length=50)
    
    def __str__(self):
        return self.rut


class Reservas(models.Model):
    ESTADOS = [
        ('ACTIVA', 'ACTIVA'),
        ('INACTIVA', 'INACTIVA'),
        ('CANCELADA', 'CANCELADA'),
    ]

    id_reserva = models.AutoField(primary_key=True)
    rut_huesped = models.ForeignKey(Huespedes, on_delete=models.PROTECT, null=True, verbose_name="Rut Huesped")
    fechaReserva = models.DateTimeField(verbose_name="Fecha Reserva", auto_now_add=True)
    num_habitacion = models.ForeignKey(Habitaciones, on_delete=models.PROTECT, null=True, verbose_name="Numero Habitacion")
    fechaIngreso = models.DateField(verbose_name="Ingreso")
    fechaSalida = models.DateField(verbose_name="Salida")
    checkout_realizado = models.BooleanField(default=False)
    estado = models.CharField(max_length=30, choices=ESTADOS)
    totalpagar = models.DecimalField(max_digits=10, decimal_places=3)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name="Usuario")

    def rese_rut(self):
        return f"Reserva {self.id_reserva} - {self.rut_huesped}"

    def calcular_total_pagar(self):
        dias_estadia = (self.fechaSalida - self.fechaIngreso).days
        precio_habitacion = Decimal(self.num_habitacion.prec_habi) if self.num_habitacion else Decimal('0.0')
        total_pagar = dias_estadia * precio_habitacion
        return total_pagar

    def save(self, *args, **kwargs):
        # Antes de guardar, calcular y asignar el total a pagar
        self.totalpagar = self.calcular_total_pagar()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id_reserva)
    
