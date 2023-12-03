from django.contrib import admin
from .models import Usuario,Habitaciones,Reservas,Huespedes
# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('rut_usu','nombre','cargo','estado')
    ordering = ('rut_usu','nombre')
    search_fields = ('nombre','rut_usu')
    #list_editable = ('nombre',)
    list_filter = ('estado',)
    #exclude = ('rut_usu',)


#admin.site.register(Usuario,UsuarioAdmin)