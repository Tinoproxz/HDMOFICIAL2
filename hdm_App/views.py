from datetime import datetime
from django.shortcuts import render, redirect
from .models import Habitaciones, Usuario,Huespedes,Reservas
from .forms import inicioSesion,regihabi,regihues,regiusu,reservar
from . import forms

# Create your views here.
def iniSesion(request):
    try:
        if request.method == 'POST':
            form = inicioSesion(request.POST)
            if form.is_valid():
                global rut_usuform
                rut_usuform = form.cleaned_data['rut_usu']
                password = form.cleaned_data['password']

                # Verifica si el usuario y la contraseña coinciden en la base de datos
                userDB = Usuario.objects.filter(rut_usu=rut_usuform, password=password)

                if userDB.exists():
                    request.session['rut_usuform'] = rut_usuform
                    # Obtiene el primer usuario encontrado
                    user = userDB.first()
                    # Redirige a diferentes menus según el tipo de usuario
                    if user.cargo == 'encargado':
                        return redirect('encargado/')  # Ajusta el nombre de la URL segun tu configuración
                    elif user.cargo == 'administrador':
                        return redirect('administrador/')  # Ajusta el nombre de la URL segun tu configuración
        else:
            form = inicioSesion()
            data = {"formulario": form,"titulo":"Inicio Sesión Hotel Duerme Bien",'nboton':'Iniciar Sesion'}
            return render(request, 'inisesion.html', data)
    except:
        data = {'r2': 'USUARIO O CONTRASEÑA INCORRECTOS',"formulario": form,"titulo":"Inicio Sesión Hotel Duerme Bien",'nboton':'Iniciar Sesion'}
        return render(request, 'inisesion.html', data)
    


#VISTAS ADMINISTRADOR
def encargado(request):
    data ={'cargo' : 'encargado','rut_usu': rut_usuform,'title':'Encargado HDM'}
    return render(request,"base.html",data)

def administrador(request):
    data ={'cargo' : 'administrador','rut_usu': rut_usuform,'title':'Administrador HDM'}
    return render(request,"base.html",data)

def usuario(request):
    admin = Usuario.objects.all()
    form = regiusu()
    if request.method == 'POST':
        form = regiusu(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/usuario') 
    data = {'data4': admin,'tabla':'Usuarios','formu':form,'rut_usu': rut_usuform,'cargo' : 'administrador','link':"/administrador"}
    return render(request, "gestion.html",data)


def eliminarUsuario(request,rut_usu):
    usu = Usuario.objects.get(rut_usu=rut_usu)
    usu.delete()
    return redirect('/usuario')

def editarUsuario(request, rut_usu):
    usu = Usuario.objects.get(rut_usu=rut_usu)
    form = regiusu(instance=usu)
    if request.method == 'POST':
        form = regiusu(request.POST, instance=usu)
        if form.is_valid():
            form.save()
            print("actualizado")
        return redirect('/usuario')   # Redirige a la vista de listar después de la edición exitosa
    data = {'tabla': 'Usuarios','formu': form, 'volver':'/usuario','rut_usu': rut_usuform,'cargo' : 'encargado','link':"/encargado"}
    return render(request,'edicion.html',data)


#VISTAS ENCARGADO

#SECCION HABITACIONES

#LEER Y AGREGAR HABITACIONES
def habitaciones(request):
    habi = Habitaciones.objects.all()
    form = regihabi()
    if request.method == 'POST':
        form = regihabi(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/habitacion') 
    data = {'data1': habi,'tabla':'Habitaciones','formu':form, 'rut_usu': rut_usuform,'cargo' : 'encargado','link':"/encargado"}
    return render(request, "gestion.html",data)

#ELIMINAR HABITACION
def eliminarHabitacion(request,num_habi):
    habi = Habitaciones.objects.get(num_habi=num_habi)
    habi.delete()
    return redirect('/habitacion',)

#EDITAR HABITACION
def editarHabitacion(request, num_habi):
    habi = Habitaciones.objects.get(num_habi=num_habi)
    form = regihabi(instance=habi)
    if request.method == 'POST':
        form = regihabi(request.POST, instance=habi)
        if form.is_valid():
            print("actualizado")
            form.save()
        return redirect('/habitacion')   # Redirige a la vista de listar después de la edición exitosa
    data = {'tabla': 'Habitaciones','formu': form, 'volver':'/habitacion','rut_usu': rut_usuform,'cargo' : 'encargado','link':"/encargado"}
    return render(request,'edicion.html',data)


#SECCION HUESPEDES
#LEER Y AGREGAR HUESPEDES
def huespedes(request):
    hues = Huespedes.objects.all()
    form = regihues()
    if request.method == 'POST':
        form = regihues(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/huesped') 
    data = {'data2': hues,'tabla':'Huespedes','formu':form, 'rut_usu': rut_usuform,'cargo' : 'encargado','link':"/encargado"}
    return render(request, "gestion.html",data)

#ELIMINAR HUESPEDES
def eliminarHuesped(request,rut):
    hues = Huespedes.objects.get(rut=rut)
    hues.delete()
    return redirect('/huesped',{'r2':'HUESPED ELIMINADO CORRECTAMENTE'})

#EDITAR HUESPEDES
def editarHuesped(request, rut):
    hues = Huespedes.objects.get(rut=rut)
    form = regihues(instance=hues)
    if request.method == 'POST':
        form = regihabi(request.POST, instance=hues)
        if form.is_valid():
            print("actualizado")
            form.save()
        return redirect('/huesped')   # Redirige a la vista de listar después de la edición exitosa
    data = {'tabla': 'Huespedes','formu': form, 'volver':'/huesped', 'rut_usu': rut_usuform,'cargo' : 'encargado','link':"/encargado"}
    return render(request,'edicion.html',data)



#LEER Y AGREGAR RESERVAS
"""def reservas(request):
    rut_usu = rut_usuform
    rese = Reservas.objects.all()
    form = reservar()

    if request.method == 'POST':
        form = reservar(request.POST)
        if form.is_valid():
            rutform = form.cleaned_data['rut']
            # Verificar si el RUT existe en la tabla de Huéspedes
            huespedex = Huespedes.objects.filter(rut=rutform).exists()

            # Asignar el valor de rut_usuform al campo correspondiente del modelo Reservas
            if huespedex:
                Reservas()
                reserva = form.save(commit=False)  # No guardar el formulario aún
                reserva = reserva.rut = rut_usu
                reserva.save()  # Ahora sí, guardar la reserva en la base de datos
        return redirect('/reserva') 

    data = {'data3': rese, 'tabla': 'Reservas', 'formu': form, 'rut_usu': rut_usuform,'cargo' : 'encargado','link':"/encargado"}
    messages.success(request, '¡Reservas listadas!')
    return render(request, "gestion.html", data)"""

def reservas(request):
    rese = Reservas.objects.all()
    forms = reservar()

    if request.method == 'POST':
        form = reservar(request.POST)
        if form.is_valid():
            # Procesar el formulario y crear la reserva
            fechaReserva = datetime.now()
            rut = form.cleaned_data['rut_huesped']
            habitacion_obj = form.cleaned_data['num_habitacion']
            fechaIngreso = form.cleaned_data['fechaIngreso']
            fechaSalida = form.cleaned_data['fechaSalida']

            # Obtener la instancia de la habitación
            habitacion = Habitaciones.objects.get(num_habi=habitacion_obj.num_habi)

            # Verificar si la habitación está disponible
            if habitacion.estado == 'disponible':
                # Obtener usuario 
                usuario = Usuario.objects.get(rut_usu=rut_usuform)

                # Crear la reserva
                reserva = Reservas.objects.create(
                    fechaReserva=fechaReserva,
                    rut_huesped=rut,
                    num_habitacion=habitacion,
                    fechaIngreso=fechaIngreso,
                    fechaSalida=fechaSalida,
                    usuario=usuario
                )
                reserva.save()

                # Marca la habitación como no disponible
                habitacion.estado = 'no disponible'
                habitacion.save()
                return redirect('/reserva') 
            else:
                print ('La habitación no está disponible en las fechas seleccionadas.')
    else:
        form = reservar()

    data = {'data3': rese, 'tabla': 'Reservas', 'formu': forms, 'rut_usu': rut_usuform, 'cargo': 'encargado', 'link': "/encargado"}
    return render(request, "gestion.html", data)



#ELIMINAR RESERVAS
def eliminarReserva(request,id_reserva):
    rese = Reservas.objects.get(id_reserva=id_reserva)
    rese.delete()
    return redirect('/reserva')

#EDITAR RESERVAS
def editarReserva(request, id_reserva):
    rese = Reservas.objects.get(id_reserva=id_reserva)
    form = reservar(instance=rese)
    if request.method == 'POST':
        form = reservar(request.POST, instance=rese)
        if form.is_valid():
            print("actualizado")
            form.save()
        return redirect('/reserva')   # Redirige a la vista de listar después de la edición exitosa
    data = {'tabla': 'Reservas','formu': form, 'volver':'/reserva','rut_usu': rut_usuform,'cargo' : 'encargado','link':"/encargado"}
    return render(request,'edicion.html',data)
