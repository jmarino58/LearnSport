from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Equipo)
admin.site.register(Categoria)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Estadistica)
admin.site.register(Alcance)
admin.site.register(Velocidad)
admin.site.register(capacidadDeSaltoVertical)