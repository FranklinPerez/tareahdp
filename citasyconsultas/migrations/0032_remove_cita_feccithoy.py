# Generated by Django 2.2.1 on 2019-06-27 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citasyconsultas', '0031_auto_20190626_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cita',
            name='fecCitHoy',
        ),
    ]