from django.db import models
from datetime import datetime

class Receitas(models.Model):
    nome_receita = models.CharField(max_length=100)
    video = models.CharField(max_length=80)
    modo_preparo = models.TextField()
    ingredientes = models.TextField()
    nota = models.IntegerField()
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    
