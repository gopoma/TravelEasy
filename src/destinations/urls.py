from django.urls import path

from . import views
app_name = "destinations"
urlpatterns = [
    path('', views.destinationsListView, name="listing"),
    path('<int:id_destination>/', views.show_details, name="detailing"),
    path('<int:id_destination>/edit/', views.destinationEditView, name="editing")
]