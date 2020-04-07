from django.db import models
from model_utils import Choices


# Usuario equivale a Custumer



class Usuario(models.Model):
    ci = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40, null=True)
    apellido = models.CharField(max_length=40, null=True)


# elimine empresa_ agregue el nombre emmpresa en Empleo. Empleo equivale a products

class Empleo(models.Model):

    GRUPO = (
        ('Hoteleria_Turismo','Hoteleria_Turismo'),
        ('Gastronomia', 'Gastronomia')
    )

    usuario = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    nombre_empresa = models.CharField(max_length=40, null=True)
    #contrato = models.IntegerField()
    fecha_ingreso = models.DateField()
    salario_nominal = models.IntegerField()
    grupo= models.CharField(max_length=200, null=True, choices=GRUPO)
    valor_dia = models.DecimalField(decimal_places=2, max_digits=5, blank=True)
    valor_hora = models.DecimalField(decimal_places=2, max_digits=5, blank=True)

    def __str__(self):
        return self.nombre_empresa

# Usuario equivale a Order

class Recibo(models.Model):

    STATUS = (
        ('Hs Extras','Hs Extras'),
        ('Hs en feriado','Hs en feriado'),
        ('Dia desc. Trabajado','Dia desc. Trabajado')
    )
    usuario = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    #empleo = models.ForeignKey(Empleo, null=True, on_delete=models.SET_NULL)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)         #revisar auto now
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    horas_extras = models.IntegerField()

    def __str__(self):
        return self.usuario