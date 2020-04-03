from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.Home, name="Home"),
    path('usuario_registro/', views.Usuario_Registro),
    path('empleo_registro/', views.Empleo_Registro)
]
