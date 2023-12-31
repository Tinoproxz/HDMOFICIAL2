# Generated by Django 4.2.5 on 2023-12-18 04:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hdm_App', '0005_alter_reservas_totalpagar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soporte',
            fields=[
                ('id_soporte', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(80)])),
                ('apellido', models.CharField(max_length=80, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(80)])),
                ('celular', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=30)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
    ]
