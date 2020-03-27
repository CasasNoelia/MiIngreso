from django.contrib import admin
from .models import Usuario, Empleo, Empresa

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Empleo)
admin.site.register(Empresa)