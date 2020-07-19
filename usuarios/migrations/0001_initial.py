# Generated by Django 3.0.5 on 2020-07-19 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('1', 'Analista de Testes'), ('2', 'Testador')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', stdimage.models.StdImageField(default='imagemUserProfile/padrao.png', upload_to='imagemUserProfile', verbose_name='Imagem')),
                ('reputacao', models.IntegerField(default=0, verbose_name='Reputação')),
                ('experiencia', models.IntegerField(default=0, verbose_name='Experiência')),
                ('role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.UserRole')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
