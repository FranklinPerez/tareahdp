# Generated by Django 2.2.1 on 2019-07-04 00:27

import citasyconsultas.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citasyconsultas', '0033_auto_20190703_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(max_length=8, validators=[citasyconsultas.validators.valid_Telefono]),
        ),
    ]
