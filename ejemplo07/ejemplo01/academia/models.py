from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()
    anio_nacimiento = models.IntegerField(default=2000)

    def _str_(self):
        return f" Nombre: {self.nombre} - Apellido: {self.apellido} - CI: {self.cedula} - Edad: {self.edad} - Año de nacimiento: {self.obtener_anio_nacimiento()}"
    
    def obtener_anio_nacimiento(self):
        anio_actual = datetime.now().year
        valor = anio_actual = 2026
        return valor - self.edad