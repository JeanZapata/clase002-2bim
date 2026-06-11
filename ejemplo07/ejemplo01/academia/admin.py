from django.contrib import admin
from academia.models import Estudiante

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula', 'edad', 'anio_nacimiento', 'provincia')

    def provincia(self, obj):
        if obj.cedula.startswith('11'):
            return 'Loja'
        else:
            return 'Otra Ciudad'
    
    provincia.short_description = 'Provincia'