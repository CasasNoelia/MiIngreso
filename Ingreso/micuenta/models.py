from django.db import models
from model_utils import Choices


# Usuario equivale a Custumer

class Usuario(models.Model):
    ci = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40, null=True)
    apellido = models.CharField(max_length=40, null=True)

# elimine empresa_ agregue el nombre emmpresa en Empleo

class Empleo(models.Model):

    GRUPO = (
        ('Hoteleria_Turismo','Hoteleria_Turismo'),
        ('Gastronomia', 'Gastronomia')
    )

    nombre_empresa = models.CharField(max_length=40, null=True)
    contrato = models.IntegerField()
    fecha_ingreso = models.DateField()
    salario_nominal = models.IntegerField()
    grupo= models.CharField(max_length=200, null=True, choices=GRUPO)
    valor_dia = models.DecimalField(decimal_places=2, max_digits=5)
    valor_hora = models.DecimalField(decimal_places=2, max_digits=5)



# Usuario equivale a Order
class Recibo(models.Model):

    STATUS = (
        ('Hs Extras','Hs Extras'),
        ('Hs en feriado','Hs en feriado'),
        ('Dia desc. Trabajado','Dia desc. Trabajado')
    )
    #Usuario =
    #Empleo =
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)         #revisar auto now
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    horas_extras = models.IntegerField()