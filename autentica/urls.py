from django.urls import path, include
from . import views

urlpatterns = [
    path("registrati/", views.registrazione, name='registrazione'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    # https://docs.djangoproject.com/en/3.1/topics/auth/default/#module-django.contrib.auth.views
]
