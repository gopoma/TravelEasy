from pydoc import classname
from django import forms
from .models import DestinoTuristico

class DestinoTuristicoForm(forms.ModelForm):
    class Meta:
        model=DestinoTuristico
        fields=[
            "nombreCiudad",
            "descripcionCiudad",
            "imagenCiudad",
            "precioTour",
            "ofertaTour"
        ]
    def clean_precioTour(self):
        precioTour = self.cleaned_data["precioTour"]
        
        if precioTour < 1:
            raise forms.ValidationError("Please provide a valid precioTour")
        return precioTour