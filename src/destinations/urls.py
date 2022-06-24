from django.urls import path

from . import views
app_name = "destinations"
urlpatterns = [
    path('', views.destinationsListView, name="listing"),
    path('create/', views.destinationCreateView, name="creating"),
    path('<int:id_destination>/', views.show_details, name="detailing"),
    path('<int:id_destination>/edit/', views.destinationEditView, name="editing"),
    path('<int:id_destination>/delete/', views.destinationDeleteView, name="deleting")
]