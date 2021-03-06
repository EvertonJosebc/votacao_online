# Generated by Django 4.0.5 on 2022-06-17 22:30

import cpf_field.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', cpf_field.models.CPFField(default='000.000.000-00', max_length=14, unique=True, verbose_name='cpf')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome Completo')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
            ],
        ),
        migrations.CreateModel(
            name='Eleicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, unique=True, verbose_name='Nome da Eleição')),
                ('data_inicial', models.DateField(verbose_name='Data Inicial')),
                ('data_final', models.DateField(verbose_name='Data Final')),
                ('candidatos', models.ManyToManyField(blank=True, to='eleicao.candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eleitor', cpf_field.models.CPFField(default='000.000.000-00', max_length=14, verbose_name='cpf')),
                ('candidato', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='eleicao.candidato')),
                ('pleito', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='eleicao.eleicao')),
            ],
        ),
    ]
