from django.urls import path

from . import views
urlpatterns = [
    path('<int:id_destination>', views.show_details, name="destination_details")
]