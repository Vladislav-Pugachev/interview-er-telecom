from django.urls import path

from . import views

urlpatterns = [
    path("<str:module>/<str:funci>/", views.index, name="index")
]
