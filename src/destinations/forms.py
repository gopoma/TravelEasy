from dataclasses import field
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
        widgets = {
            "nombreCiudad": forms.TextInput(attrs={
                "class": "form__regular-input"
            }),
            "descripcionCiudad": forms.Textarea(attrs={
                "class": "form__textarea",
                "rows": 4,
                "cols": 36
            }),
            "imagenCiudad": forms.FileInput(attrs={
                "class": "form__file-input"
            }),
            "precioTour": forms.NumberInput(attrs={
                "class": "form__regular-input"
            }),
            "ofertaTour": forms.CheckboxInput(attrs={
                "class": "form__checkbox-input"
            })
        }
    def clean_precioTour(self):
        precioTour = self.cleaned_data["precioTour"]
        
        if precioTour < 1:
            raise forms.ValidationError("Please provide a valid precioTour")
        return precioTour