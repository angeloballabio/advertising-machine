from django.shortcuts import render



# Create your views here.
def mostrapubblicita(request):
    return render(request, "mostrapubblicita/mostra_pubblicita.html")