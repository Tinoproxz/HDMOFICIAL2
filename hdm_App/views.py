from datetime import datetime
from django.shortcuts import render, redirect,get_object_or_404
from .models import Habitaciones, Usuario,Huespedes,Reservas
from .forms import inicioSesion,regihabi,regihues,regiusu,reservar, contacto, MetodoPagoForm, CHECKOUT
from django.contrib import messages
from django.shortcuts import render
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
                userDB = Usuario.objects.filter(rut_usu=rut_usuform, password=password, estado='activo')

                if userDB.exists():
                    request.session['rut_usuform'] = rut_usuform
                    # Obtiene el usuario encontrado
                    user = userDB.first()
                    
                    if user.cargo == 'encargado':
                        return redirect('encargado/')  
                    elif user.cargo == 'administrador':
                        return redirect('administrador/') 
                else:
                    messages.error(request, 'Usuario no activo o credenciales incorrectas.')
        else:
            form = inicioSesion()
            data = {"formulario": form, "titulo": "Inicio Sesión Hotel Duerme Bien", 'nboton': 'Iniciar Sesion'}
            return render(request, 'inisesion.html', data)
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
    
    data = {"formulario": form, "titulo": "Inicio Sesión Hotel Duerme Bien", 'nboton': 'Iniciar Sesion'}
    return render(request, 'inisesion.html', data)
    

#VISTAS ADMINISTRADOR
def soporte (request):
    form = contacto()
    if request.method == 'POST':
        form = contacto(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pronto nos pondremos en contacto para resolver su petición.')
        return redirect('/home')
    data = {'formu':form,'volver':'/home','rut_usu': rut_usuform,'cargo' : 'encargado','link':"/encargado"}
    return render (request,"contacto.html",data)

def encargado(request):
    habitaciones_filtradas = Habitaciones.objects.all()
    data ={'data1': habitaciones_filtradas,'cargo' : 'encargado','rut_usu': rut_usuform,'title':'Encargado HDM'}
    return render(request,"mains.html",data)

def administrador(request):
    data ={'cargo' : 'administrador','rut_usu': rut_usuform,'title':'Administrador HDM'}
    return render(request,"mains.html",data)

def usuario(request):
    admin = Usuario.objects.all()
    estados = Usuario.objects.values_list('estado', flat=True).distinct()
    form = regiusu()
    if request.method == 'POST':
        form = regiusu(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/usuario') 
    data = {'data4': admin,'tabla':'Usuarios','formu':form,'rut_usu': rut_usuform,'cargo' : 'administrador','link':"/administrador",'estados':estados}
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
        return redirect('/usuario')   
    data = {'tabla': 'Usuarios','formu': form, 'volver':'/usuario','rut_usu': rut_usuform,'cargo' : 'encargado','link':"/encargado"}
    return render(request,'edicion.html',data)


#VISTAS ENCARGADO

#SECCION HABITACIONES

#LEER Y AGREGAR HABITACIONES
def habitaciones(request):
    habitaciones_filtradas = Habitaciones.objects.all()
    estado_param = request.GET.get('estado__exact')
    precio_param = request.GET.get('prec_habi__exact')
    capacidad_param = request.GET.get('capacidad__exact')

    if estado_param:
        habitaciones_filtradas = habitaciones_filtradas.filter(estado=estado_param)
    if precio_param:
        habitaciones_filtradas = habitaciones_filtradas.filter(prec_habi=precio_param)
    if capacidad_param:
        habitaciones_filtradas = habitaciones_filtradas.filter(capacidad=capacidad_param)

    form = regihabi()
    if request.method == 'POST':
        form = regihabi(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/habitacion') 

    data = {'data1': habitaciones_filtradas,'tabla': 'Habitaciones','formu': form,'rut_usu': rut_usuform,'cargo': 'encargado','link': "/encargado"}
    return render(request, "gestion.html", data)

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
        return redirect('/habitacion')   
    data = {'tabla': 'Habitaciones','formu': form, 'volver':'/habitacion','rut_usu': rut_usuform,'cargo' : 'encargado','link':"/encargado"}
    return render(request,'edicion.html',data)


#SECCION HUESPEDES
#LEER Y AGREGAR HUESPEDES
def huespedes(request):
    hues = Huespedes.objects.all()
    residencia = Huespedes.objects.values_list('residencia', flat=True).distinct()
    residencia_param = request.GET.get('residencia__exact')

    if residencia_param:
        hues = hues.filter(residencia=residencia_param)

    form = regihues()
    if request.method == 'POST':
        form = regihues(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/huesped') 
    data = {'data2': hues,'tabla':'Huespedes','formu':form, 'rut_usu': rut_usuform,'cargo' : 'encargado','link':"/encargado",'residencias': residencia}
    return render(request, "gestion.html",data)

#ELIMINAR HUESPEDES
def eliminarHuesped(request,rut):
    hues = Huespedes.objects.get(rut=rut)
    hues.delete()
    return redirect('/huesped')

#EDITAR HUESPEDES
def editarHuesped(request, rut):
    hues = Huespedes.objects.get(rut=rut)
    form = regihues(instance=hues)
    if request.method == 'POST':
        form = regihues(request.POST, instance=hues)
        if form.is_valid():
            form.save()
            print("actualizado")
        return redirect('/huesped')   
    data = {'tabla': 'Huespedes','formu': form, 'volver':'/huesped','rut_usu': rut_usuform,'cargo' : 'encargado','link':"/encargado"}
    return render(request,'edicion.html',data)



#LEER Y AGREGAR RESERVAS
def reservas(request):
    rese = Reservas.objects.all()
    usuarios = Reservas.objects.values_list('usuario', flat=True).distinct()
    habitaciones = Reservas.objects.values_list('num_habitacion', flat=True).distinct()

    usuario_param = request.GET.get('usuario__exact')
    habitacion_param = request.GET.get('num_habitacion__exact')

    if usuario_param:
        rese = rese.filter(usuario=usuario_param)
    if habitacion_param:
        rese = rese.filter(num_habitacion=habitacion_param)

    forms = reservar()

    if request.method == 'POST':
        form = reservar(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut_huesped']
            habitacion_obj = form.cleaned_data['num_habitacion']
            fechaIngreso = form.cleaned_data['fechaIngreso']
            fechaSalida = form.cleaned_data['fechaSalida']
            estado = form.cleaned_data['estado']

            if not Huespedes.objects.filter(rut=rut).exists():
                messages.error(request, 'El RUT del huésped no existe en la base de datos.')
                return redirect('/reserva')

            habitacion = Habitaciones.objects.get(num_habi=habitacion_obj.num_habi)

            if habitacion.estado == 'disponible':
                usuario = Usuario.objects.get(rut_usu=rut_usuform)

                reserva = Reservas.objects.create(
                    rut_huesped=rut,
                    num_habitacion=habitacion,
                    fechaIngreso=fechaIngreso,
                    fechaSalida=fechaSalida,
                    estado=estado,
                    usuario=usuario
                )

                return redirect('/reserva') 
            else:
                messages.error(request, 'La habitación no está disponible en las fechas seleccionadas.')
    else:
        form = reservar()

    data = {'data3': rese, 'tabla': 'Reservas', 'formu': forms, 'rut_usu': rut_usuform, 'cargo': 'encargado', 'link': "/encargado",
            'usuarios': usuarios, 'habitaciones': habitaciones}
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
        return redirect('/reserva')
    data = {'tabla': 'Reservas','formu': form, 'volver':'/reserva','rut_usu': rut_usuform,'cargo' : 'encargado','link':"/encargado"}
    return render(request,'edicion.html',data)

def checkout(request, id_reserva):
    reserva_instance = get_object_or_404(Reservas, id_reserva=id_reserva)

    if request.method == 'POST':
        form_reserva = reservar(request.POST, instance=reserva_instance)
        form_pago = CHECKOUT(request.POST)

        if form_reserva.is_valid() and form_pago.is_valid():
            form_reserva.save()

            metodo_pago = form_pago.cleaned_data['metodo_pago']


            reserva_instance.estado = 'cancelado'
            reserva_instance.save()

            habitacion_asociada = reserva_instance.num_habitacion
            if habitacion_asociada:

                habitacion_asociada.estado = 'en mantenimiento'
                habitacion_asociada.save()

            return redirect('/reserva')

    else:
        form_reserva = reservar(instance=reserva_instance)
        form_pago = CHECKOUT(initial={'id_reserva': id_reserva})

    data = {
        'form_reserva': form_reserva,
        'form_pago': form_pago,
        'reserva': reserva_instance,
        'volver': '/reserva',
        'cargo': 'encargado',
        'link': "/encargado",
    }

    return render(request, 'checkout.html', data)