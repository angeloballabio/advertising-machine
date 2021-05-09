from django import forms
from creapubblicita.models import Cartella


class CartellaModelForm(forms.ModelForm):

    class Meta:
        model = Cartella
        fields = ['nome_cartella', 'tempo_riproduzione']
        widjets = {
            "nome_cartella" : forms.TextInput(attrs={"class": "form-control"}),
            "tempo_riproduzione" : forms.NumberInput(attrs={"class": "form-control"}),
        }
        labels = {
            "nome_cartella": "nome della cartella pubblicitaria",
            "tempo_riproduzione": "Tempo di riproduzione messaggio",
        }

    def __init__(self) -> None:
        super().__init__()