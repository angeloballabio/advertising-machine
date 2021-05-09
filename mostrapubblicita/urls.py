from django.urls import path
from . import views


urlpatterns = [
    path("mostrapubblicita/", views.mostrapubblicita, name='mostra_pubblicita'),
]