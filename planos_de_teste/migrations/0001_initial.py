# Generated by Django 3.0.5 on 2020-07-19 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanoDeTeste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_plano_de_teste', models.CharField(max_length=150, verbose_name='Nome do Plano de Testes')),
                ('tipo_produto', models.CharField(max_length=100, verbose_name='Tipo do Produto')),
                ('nome_produto', models.CharField(max_length=100, verbose_name='Nome do Produto')),
                ('url_acesso', models.CharField(max_length=255, verbose_name='URL de acesso')),
                ('descricao_produto', models.TextField(verbose_name='Descrição do Produto')),
                ('tipo_de_teste_a_ser_executado', models.CharField(max_length=100, verbose_name='Tipo de teste a ser executado')),
                ('modelo_remuneracao', models.CharField(max_length=100, verbose_name='Modelo da remuneração')),
                ('detalhes_de_autenticacao_no_produto', models.TextField(max_length=255, verbose_name='Detalhes de autenticação no produto')),
                ('versao_do_produto', models.CharField(blank=True, max_length=255, verbose_name='Versão do Produto')),
                ('estado_do_lancamento_do_produto', models.CharField(max_length=255, verbose_name='Estado do lançamento do produto')),
                ('analista_de_testes', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=100, verbose_name='País')),
                ('plano_de_teste', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='planos_de_teste.PlanoDeTeste')),
            ],
        ),
        migrations.CreateModel(
            name='Operadora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operadora', models.CharField(max_length=50, verbose_name='Operadora')),
                ('plano_de_teste', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='planos_de_teste.PlanoDeTeste')),
            ],
        ),
        migrations.CreateModel(
            name='Navegador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navegador', models.CharField(max_length=80, verbose_name='Navegador')),
                ('versao', models.CharField(max_length=50, verbose_name='Versão')),
                ('plano_de_teste', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='planos_de_teste.PlanoDeTeste')),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(max_length=100, verbose_name='Idioma')),
                ('plano_de_teste', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='planos_de_teste.PlanoDeTeste')),
            ],
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispositivo', models.CharField(max_length=100, verbose_name='Tipo do dispositivo')),
                ('sistema_operacional', models.CharField(max_length=80, verbose_name='Sistema Operacional a ser testado')),
                ('plano_de_teste', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='planos_de_teste.PlanoDeTeste')),
            ],
        ),
    ]
