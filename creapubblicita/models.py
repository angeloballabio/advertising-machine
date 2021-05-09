from django.db import models


# Create your models here.
class Cartella(models.Model):
    nome_cartella = models.CharField(max_length=128, help_text='inserire nome cartella')
    tempo_riproduzione = models.IntegerField(help_text="secondi di riproduzione")

    def __str__(self):
        return self.nome_cartella

    class Meta:
        verbose_name = 'Cartella'
        verbose_name_plural = 'Cartelle'