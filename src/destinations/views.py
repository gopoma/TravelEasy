from django.shortcuts import render
from django.http import HttpResponse
from .models import DestinoTuristico

# Create your views here.
def home(request):
    destinations = DestinoTuristico.objects.all()
    return render(request, "home.html", {"destinations": destinations})

def destinationsListView(request):
    if not request.user.is_authenticated:
        return render(request, "notAllowed.html")

    destinations = DestinoTuristico.objects.all()
    return render(request, "destinations/destinations.html", {
        "destinations": destinations
    })

def show_details(request, id_destination):
    if not request.user.is_authenticated:
        return render(request, "notAllowed.html")

    if not DestinoTuristico.objects.filter(id=id_destination).exists():
        return HttpResponse("Not Found...")

    destination = DestinoTuristico.objects.get(id=id_destination)
    return render(request, "destinations/destination.html", {"destination": destination})