# Generated by Django 2.2.1 on 2019-06-23 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citasyconsultas', '0025_auto_20190623_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='estado',
            field=models.IntegerField(default=0, help_text='Activa (0), Completada (1)', null=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='duraci',
            field=models.CharField(max_length=10),
        ),
    ]
