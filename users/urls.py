
from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', LogoutView.as_view(template_name="AppCoder/inicio.html"), name="logout"),
    path('editar_perfil/', views.editar_perfil, name="editar_perfil"),
    path('editar_pass/', views.PasswordChange.as_view(), name="editar_pass"),
]
