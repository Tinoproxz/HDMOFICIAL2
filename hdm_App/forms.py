from django import forms
from .models import Usuario,Habitaciones,Huespedes,Reservas

#CLASES ADMINISTRADOR
#CLASE DE INICIO DE SESION PARA EL SISTEMA
class inicioSesion(forms.Form):
    rut_usu = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    rut_usu.widget.attrs['class'] = 'form-control'
    password.widget.attrs['class'] = 'form-control'

#FORMULARIO PARA REGISTRAR Y ACTUALIZAR UN USUARIO (SOLO LO PUEDE HACER EL ADMINISTRADOR)
class regiusu(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut_usu', 'nombre', 'apellidos', 'cargo', 'password', 'estado']
        widgets = {
            'rut_usu': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }


#CLASES DE ENCARGADO
#HABITACIONES
#CLASE REGISTRAR HABITACION (ENCARGADO)
class regihabi(forms.ModelForm):
    class Meta:
        model = Habitaciones
        fields = ['num_habi', 'estado', 'orientacion', 'prec_habi', 'capacidad']
        widgets = {
            'num_habi': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'orientacion': forms.Select(attrs={'class': 'form-control'}),
            'prec_habi': forms.Select(attrs={'class': 'form-control'}),
            'capacidad': forms.Select(attrs={'class': 'form-control'}),
        }


#HUESPEDES
class regihues(forms.ModelForm):
    class Meta:
        model = Huespedes
        fields = ['rut', 'nombre', 'apellidos', 'correo', 'num_telefono','residencia']
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'num_telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'residencia': forms.TextInput(attrs={'class': 'form-control'}),
        }

#RESERVAS
class reservar(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = ['rut_huesped', 'num_habitacion', 'fechaIngreso', 'fechaSalida']
        widgets = {
            'rut_huesped': forms.TextInput(attrs={'class': 'form-control'}),
            'num_habitacion': forms.Select(attrs={'class': 'form-control'}),
            'fechaIngreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fechaSalida': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }











    













    







    