from django.db import models
from clubes.models import Clube

class Membro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)

def __str__(self):
    return f"{self.nome} ({self.clube.nome})"

# Create your models here.
