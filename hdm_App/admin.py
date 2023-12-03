from django.contrib import admin
from .models import Usuario,Habitaciones,Reservas,Huespedes
# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('rut_usu','mayunombre','cargo','estado')
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

#admin.site.register(Usuario,UsuarioAdmin)