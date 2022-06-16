from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Fallback")
    # destinations = DestinosTuristicos.objects.all()
    # return render(request, "home.html", {"destinations": destinations})