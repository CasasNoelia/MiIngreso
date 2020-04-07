from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.Home, name="Home"),
    path('usuario/<str:pk_test>/', views.Usuario, name="usuario"),
    path('informacion/', views.Informacion, name="informacion"),
    path('empleo/',views.Empleo, name="empleo"),
    path('recibo/', views.Recibo,  name="recibo")
]
