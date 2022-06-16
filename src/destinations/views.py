from django.shortcuts import render
# from .models import Destination
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Fallback")
# destinations = Destination.objects.all()
# return render(request, "home.html", {"destinations": destinations})