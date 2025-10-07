from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    edad= models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.email}"
    
