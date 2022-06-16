from django.db import models

# Create your models here.
class DestinoTuristico(models.Model):
    nombreCiudad = models.CharField(max_length=255)
    descripcionCiudad = models.TextField()
    imagenCiudad = models.ImageField(upload_to="pics")
    precioTour = models.FloatField()
    ofertaTour = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombreCiudad} [Is on offer?: {self.ofertaTour}]"