from django.db import models
from django.urls import reverse

# Create your models here.
class DestinoTuristico(models.Model):
    nombreCiudad = models.CharField(max_length=255)
    descripcionCiudad = models.TextField()
    imagenCiudad = models.ImageField(upload_to="pics")
    precioTour = models.FloatField()
    ofertaTour = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("destinations:detailing", kwargs={"id_destination": self.id})
    def __str__(self):
        return f"{self.nombreCiudad}"