from django.db import models

# Create your models here.


class Usuario(models.Model):
    ci = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)


class Empresa(models.Model):

    rut = models.IntegerField(primary_key=True)

class Empleo(models.Model):

    contrato = models.IntegerField()
    fecha_ingreso = models.DateField()
    salario_nominal = models.IntegerField()
    valor_dia = models.DecimalField(decimal_places=2, max_digits=5)
    valor_hora = models.DecimalField(decimal_places=2, max_digits=5)

class Recibo(models.Model):

    horas_extras = models.IntegerField()