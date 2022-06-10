from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="pics")
    description = models.TextField()
    price = models.FloatField()
    is_on_offer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} [Is on offer?: {self.is_on_offer}]"