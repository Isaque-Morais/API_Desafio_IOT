# Generated by Django 3.2.9 on 2021-11-14 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cupom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_cupom', models.CharField(max_length=8)),
                ('cnpj', models.CharField(max_length=14)),
                ('valor_compra', models.CharField(max_length=8)),
                ('data', models.DateField()),
                ('entidade_doacao', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ModeloNota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_nota', models.CharField(max_length=8)),
                ('descricao', models.CharField(max_length=100)),
                ('tipos', models.CharField(choices=[('C', 'Cumpom Fiscal'), ('N', 'Nota Fiscal')], default='C', max_length=1)),
            ],
        ),
    ]