from django.shortcuts import render
from .models import DestinoTuristico
from django.http import HttpResponse

# Create your views here.
def home(request):
    destinations = DestinoTuristico.objects.all()
    return render(request, "home.html", {"destinations": destinations})

def show_details(request, id_destination):
    return HttpResponse(f"Target destination's id: {id_destination}")