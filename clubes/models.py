from django.db import models
from django.contrib.auth.models import User

class Clube(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.nome

# Create your models here.
