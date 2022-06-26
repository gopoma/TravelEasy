from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import DestinoTuristico
from .forms import DestinoTuristicoForm

# Create your views here.
def home(request):
    destinations = DestinoTuristico.objects.all().order_by("-id")
    return render(request, "home.html", {"destinations": destinations})

def destinationsListView(request):
    if not request.user.is_staff:
        return render(request, "notAllowed.html")

    destinations = DestinoTuristico.objects.all().order_by("-id")
    return render(request, "destinations/destinations.html", {
        "destinations": destinations
    })

def show_details(request, id_destination):
    if not request.user.is_authenticated:
        return render(request, "notAllowed.html")

    destination = get_object_or_404(DestinoTuristico, id=id_destination)
    return render(request, "destinations/destination.html", {"destination": destination})

def destinationCreateView(request):
    if not request.user.is_staff:
        return render(request, "notAllowed.html")
    create_form = DestinoTuristicoForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if create_form.is_valid():
            create_form.save()
            return redirect("/destinations")
    return render(request, "destinations/create.html", { "create_form": create_form })

def destinationEditView(request, id_destination):
    if not request.user.is_staff:
        return render(request, "notAllowed.html")
    
    destination = get_object_or_404(DestinoTuristico, id=id_destination)
    edit_form = DestinoTuristicoForm(request.POST or None, request.FILES or None, instance=destination)
    if request.method == "POST" and edit_form.is_valid():
        edit_form.save()
        return redirect("/destinations")
    return render(request, "destinations/edit.html", { "edit_form": edit_form })

def destinationDeleteView(request, id_destination):
    if not request.user.is_staff:
        return render(request, "notAllowed.html")
    destination = get_object_or_404(DestinoTuristico, id=id_destination)

    if request.method == "POST":
        destination.delete()
        return redirect("/destinations")
    return render(request, "destinations/delete.html", {
        "destination": destination
    })

def search(request):
    nombreCiudad = request.GET.get("nombreCiudad")
    ofertaTour = request.GET.get("ofertaTour")
    queryBody = {}
    
    if nombreCiudad is not None:
        queryBody = {
            **queryBody,
            "nombreCiudad": nombreCiudad
        }
    if ofertaTour is not None:
        queryBody = {
            **queryBody,
            "ofertaTour": ofertaTour == "on" or ofertaTour == "true" or ofertaTour == "1"
        }
    destinations = DestinoTuristico.objects.filter(**queryBody)
    return render(request, "destinations/destinations.html", {
        "destinations": destinations
    })