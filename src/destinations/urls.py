from django.urls import path

from . import views
urlpatterns = [
    path('', views.destinationsListView, name="listing"),
    path('<int:id_destination>', views.show_details, name="destination_details")
]