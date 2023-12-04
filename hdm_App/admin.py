from django.contrib import admin
from .models import Usuario,Habitaciones,Reservas,Huespedes
# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('rut_usu','mayunombre','cargo','password','estado',)
    #ordering = ('rut_usu','nombre')
    search_fields = ('nombre','rut_usu')
    #list_editable = ('nombre',)
    list_filter = ('estado',)
    #exclude = ('rut_usu',)
    fieldsets = (
        (None,{
            'fields': ('nombre',)
        }),
        ('Advanced options',
            {
                'classes':('collapse','wide','extrapretty'),
                'fields':('rut_usu',)
            }
        )
    )
    def mayunombre(self,obj):
        return obj.nombre.upper()
    mayunombre.short_description = "Nombre (MAYUS)"

    mayunombre.admin_order_field = 'nombre'

@admin.register(Habitaciones)
class HabitacionAdmin(admin.ModelAdmin):
    list_display=('num_habi','estado','orientacion','prec_habi','capacidad')
    search_fields = ('num_habi','capacidad','prec_habi')
    list_filter = ('estado','prec_habi','capacidad')

@admin.register(Huespedes)
class HuespedAdmin(admin.ModelAdmin):
    list_display=('rut','nombre','apellidos','correo','num_telefono','residencia')
    search_fields = ('rut','nombre','apellidos',)
    list_filter = ('residencia',)

@admin.register(Reservas)
class ReservasAdmin(admin.ModelAdmin):
    list_display=('id_reserva','rut_huesped','fechaReserva','num_habitacion','fechaIngreso','fechaSalida','usuario','checkout_realizado',)
    search_fields = ('rut_huesped','id_reserva',)
    list_filter = ('usuario','checkout_realizado',)

#admin.site.register(Usuario,UsuarioAdmin)