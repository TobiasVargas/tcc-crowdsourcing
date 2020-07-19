from django.db import models
from planos_de_teste.models import PlanoDeTeste

class CenarioDeTeste(models.Model):
    titulo = models.CharField(max_length=150)
    plano_de_teste = models.ForeignKey(PlanoDeTeste, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo