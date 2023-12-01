from django.urls import path
from . import views
urlpatterns = [
    path('', views.iniSesion),
    path('administrador/', views.administrador),
    path('encargado/',views.encargado),
    # HABITACION
    path('habitacion/',views.habitaciones),
    path('eliminarHabitacion/<int:num_habi>',views.eliminarHabitacion),
    path('editarHabitacion/<int:num_habi>', views.editarHabitacion),

    # HUESPED
    path('huesped/',views.huespedes),
    path('eliminarHuesped/<int:rut>',views.eliminarHuesped),
    path('editarHuesped/<int:rut>', views.editarHuesped),

    # RESERVA
    path('reserva/',views.reservas),
    path('eliminarHuesped/<int:rut>',views.eliminarReserva),
    path('editarHuesped/<int:rut>', views.editarReserva),

    # ADMINISTRADOR
    path('usuario/',views.usuario),
    path('eliminarUsuario/<int:rut_usu>',views.eliminarUsuario),
    path('editarUsuario/<int:rut_usu>', views.editarUsuario),
]
