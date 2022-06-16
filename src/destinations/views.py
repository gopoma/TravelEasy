from django.shortcuts import render
from .models import DestinoTuristico

# Create your views here.
def home(request):
    destinations = DestinoTuristico.objects.all()
    return render(request, "home.html", {"destinations": destinations})