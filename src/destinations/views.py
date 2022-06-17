from django.shortcuts import render
from .models import DestinoTuristico

# Create your views here.
def home(request):
    destinations = DestinoTuristico.objects.all()
    return render(request, "home.html", {"destinations": destinations})

def show_details(request, id_destination):
    return render(request, "destinations/destination.html", {"id_destination": id_destination})