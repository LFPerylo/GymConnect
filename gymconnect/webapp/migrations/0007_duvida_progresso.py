# Generated by Django 5.0.2 on 2024-05-06 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_progressoaluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duvida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duvida_escrita', models.TextField()),
                ('nome_treinador', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Progresso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_aluno', models.CharField(max_length=100)),
                ('metrica', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('progresso_observado', models.TextField()),
            ],
        ),
    ]
