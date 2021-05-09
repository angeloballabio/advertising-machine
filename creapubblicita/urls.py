from django.urls import path
from . import views


urlpatterns = [
    path("creapubblicita/", views.creapubblicita, name='crea_pubblicita'),
]