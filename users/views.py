from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
#from .forms import UserRegisterForm, UserEditForm, AvatarFormulario


# Create your views here.
def login_request(request):

    msg_login = ""
    data = None
    if request.method == 'POST':
        data = request.POST
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                return render(request, "AppCoder/inicio.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm(None, data)
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})


def register(request):

    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"AppCoder/inicio.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})


# Vista de editar el perfil
# Obligamos a loguearse para editar los datos del usuario activo
@login_required
def editar_perfil(request):

    # El usuario para poder editar su perfil primero debe estar logueado.
    # Al estar logueado, podremos encontrar dentro del request la instancia
    # del usuario -> request.user
    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, instance=request.user)

        if miFormulario.is_valid():

            miFormulario.save()

            # Retornamos al inicio una vez guardado los datos
            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario = UserEditForm(instance=request.user)

    return render(
        request,
        "users/editar_usuario.html",
        {
            "mi_form": miFormulario,
            "usuario": usuario
        }
    )


class PasswordChange(LoginRequiredMixin, PasswordChangeView):

    template_name = "users/editar_pass.html"
    success_url = reverse_lazy('editar_perfil')


# @login_required
# def agregar_avatar(request):
    
#     if request.method == "POST":
#         mi_form = AvatarFormulario(request.POST, request.FILES)
    
#         if mi_form.is_valid():
#             user = User.objects.get(username=request.user)
#             avatar = Avatar(user=user, imagen=mi_form.cleaned_data['imagen'])
#             avatar.save()
            
#             return render(request, "AppCocer/index.html")
#     else:
#         mi_form = AvatarFormulario()
    
#     context_data = {"mi_form": mi_form}
#     return render(request, "users/agregar_avatar.html", context_data)
