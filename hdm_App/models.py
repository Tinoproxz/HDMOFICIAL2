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
        return str(self.num_habi) + ' ( Capacidad: ' + self.capacidad + ' /  Orientacion: '+ self.orientacion +' ) '
        

class Huespedes(models.Model):
    rut = models.CharField(primary_key=True,max_length=12,validators=[validators.MinLengthValidator(9), validators.MaxLengthValidator(12)])
    nombre = models.CharField(max_length=80,validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(80)])
    apellidos = models.CharField(max_length=80,validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(80)])
    correo = models.EmailField()
    num_telefono = models.CharField(max_length=12,validators=[validators.MaxLengthValidator(12), validators.MinLengthValidator(9)],verbose_name="Numero Telefono")
    residencia = models.CharField(max_length=50)

class Reservas(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    rut = models.ForeignKey(Huespedes, on_delete = models.SET_NULL, null = True, verbose_name="Rut Huesped")
    fechaReserva = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Reserva")
    num_habi = models.ForeignKey(Habitaciones, on_delete = models.SET_NULL, null = True,verbose_name="Numero Habitacion")
    fechaIngreso = models.DateField(verbose_name="Ingreso")
    fechaSalida = models.DateField(verbose_name="Salida")
    rut_usu = models.ForeignKey(Usuario, on_delete = models.SET_NULL, null = True,verbose_name="Usuario")