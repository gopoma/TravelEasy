from django.shortcuts import render
from .models import Destination

# Create your views here.
def home(request):
    destinations = Destination.objects.all()

    return render(request, "home.html", {"destinations": destinations})