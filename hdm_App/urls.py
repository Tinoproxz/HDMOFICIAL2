from django.urls import path
from . import views
urlpatterns = [
    path('', views.iniSesion),
    path('contacto/', views.soporte),
    path('administrador/', views.administrador),
    path('encargado/',views.encargado),
    # HABITACION
    path('habitacion/',views.habitaciones),
    path('eliminarHabitacion/<int:num_habi>',views.eliminarHabitacion),
    path('editarHabitacion/<int:num_habi>', views.editarHabitacion),

    # HUESPED
    path('huesped/', views.huespedes),
    path('eliminarHuesped/<str:rut>/', views.eliminarHuesped),
    path('editarHuesped/<str:rut>/', views.editarHuesped),

    # RESERVA
    path('reserva/',views.reservas),
    path('eliminarReserva/<int:id_reserva>',views.eliminarReserva),
    path('editarReserva/<int:id_reserva>', views.editarReserva),
    path('checkoutReserva/<int:id_reserva>', views.checkout),
    

    # ADMINISTRADOR
    path('usuario/',views.usuario),
    path('eliminarUsuario/<int:rut_usu>',views.eliminarUsuario),
    path('editarUsuario/<int:rut_usu>', views.editarUsuario),
]
