# Generated by Django 2.2.1 on 2019-06-22 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citasyconsultas', '0017_auto_20190622_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='estado',
            field=models.IntegerField(default=0, help_text='Pendiente = 0 ,  Completado = 1', null=True),
        ),
    ]
