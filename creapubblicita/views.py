from creapubblicita.forms import CartellaModelForm
from django.shortcuts import render
from creapubblicita.models import Cartella

# Create your views here.
def creapubblicita(request):
    
        
    cartelle = Cartella.objects.all()
    context = {'cartelle': cartelle}
    return render(request, "creapubblicita/crea_pubblicita.html", context)

def modifica_voce(request, pk):
    if request.method == "POST":
        form = CartellaModelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        return render(request)