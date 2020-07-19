from django.db import models
from django.contrib.auth.models import User

class PlanoDeTeste(models.Model):
    nome_plano_de_teste = models.CharField('Nome do Plano de Testes', max_length=150)
    tipo_produto = models.CharField('Tipo do Produto', max_length=100)
    nome_produto = models.CharField('Nome do Produto', max_length=100)
    url_acesso = models.CharField('URL de acesso', max_length=255)
    descricao_produto = models.TextField('Descrição do Produto')
    tipo_de_teste_a_ser_executado = models.CharField('Tipo de teste a ser executado', max_length=100)
    modelo_remuneracao = models.CharField('Modelo da remuneração', max_length=100)
    detalhes_de_autenticacao_no_produto = models.TextField('Detalhes de autenticação no produto', max_length=255)
    versao_do_produto = models.CharField('Versão do Produto', max_length=255, blank=True)
    estado_do_lancamento_do_produto = models.CharField('Estado do lançamento do produto', max_length=255)
    analista_de_testes = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_plano_de_teste


class Dispositivo(models.Model):
    dispositivo = models.CharField('Tipo do dispositivo', max_length=100)
    sistema_operacional = models.CharField('Sistema Operacional a ser testado', max_length=80)
    plano_de_teste = models.ForeignKey(PlanoDeTeste, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.dispositivo


class Navegador(models.Model):
    navegador = models.CharField('Navegador', max_length=80)
    versao = models.CharField('Versão', max_length=50)
    plano_de_teste = models.ForeignKey(PlanoDeTeste, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.navegador


class Pais(models.Model):
    pais = models.CharField('País', max_length=100)
    plano_de_teste = models.ForeignKey(PlanoDeTeste, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.pais


class Operadora(models.Model):
    operadora = models.CharField('Operadora', max_length=50)
    plano_de_teste = models.ForeignKey(PlanoDeTeste, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.operadora


class Idioma(models.Model):
    idioma = models.CharField('Idioma', max_length=100)
    plano_de_teste = models.ForeignKey(PlanoDeTeste, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.idioma