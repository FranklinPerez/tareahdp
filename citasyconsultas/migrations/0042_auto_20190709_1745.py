# Generated by Django 2.2.1 on 2019-07-09 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citasyconsultas', '0041_auto_20190709_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='numCit',
            field=models.IntegerField(error_messages={'unique': 'Ya existe una Cita con este numero'}, help_text='Numero de cita del dia', primary_key=True, serialize=False),
        ),
    ]