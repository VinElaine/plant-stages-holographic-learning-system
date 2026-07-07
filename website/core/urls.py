from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("stages/", views.stages, name="stages"),
    path("viewer/<int:stage_id>/", views.viewer, name="viewer"),
    path("hologram/<int:stage_id>/", views.hologram, name="hologram"),
]