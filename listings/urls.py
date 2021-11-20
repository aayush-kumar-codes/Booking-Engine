from django.urls import path

from . import views
# survey/
urlpatterns = [
    path("units/", views.AvailableRoomsView.as_view()),
    
]
