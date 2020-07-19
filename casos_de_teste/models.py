from django.db import models
from cenarios_de_teste.models import CenarioDeTeste


class CasoDeTeste(models.Model):
    cenario_de_teste = models.ForeignKey(CenarioDeTeste, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    objetivo_do_teste = models.CharField(max_length=255)
    resultado = models.CharField(max_length=150, null=True, blank=True)
    data_de_execucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo


class PreCondicao(models.Model):
    pre_condicao = models.CharField(max_length=255)
    casoDeTeste = models.ForeignKey(CasoDeTeste, on_delete=models.CASCADE)

    def __str__(self):
        return self.pre_condicao


class Acoes(models.Model):
    acoes_do_passo = models.CharField(max_length=255)
    resultados_esperados = models.CharField(max_length=255, null=True, blank=True)
    casoDeTeste = models.ForeignKey(CasoDeTeste, on_delete=models.CASCADE)

    def __str__(self):
        return self.acoes_do_passo