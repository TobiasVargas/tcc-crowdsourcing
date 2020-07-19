# Generated by Django 3.0.5 on 2020-07-19 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planos_de_teste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasoDeTeste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('objetivo_do_teste', models.CharField(max_length=255)),
                ('resultado', models.CharField(blank=True, max_length=150, null=True)),
                ('data_de_execucao', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PreCondicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pre_condicao', models.CharField(max_length=255)),
                ('casoDeTeste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cenarios_de_teste.CasoDeTeste')),
            ],
        ),
        migrations.CreateModel(
            name='CenarioDeTeste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('plano_de_teste', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='planos_de_teste.PlanoDeTeste')),
            ],
        ),
        migrations.AddField(
            model_name='casodeteste',
            name='cenarioDeTeste',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cenarios_de_teste.CenarioDeTeste'),
        ),
        migrations.CreateModel(
            name='Acoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acoes_do_passo', models.CharField(max_length=255)),
                ('resultados_esperados', models.CharField(blank=True, max_length=255, null=True)),
                ('casoDeTeste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cenarios_de_teste.CasoDeTeste')),
            ],
        ),
    ]