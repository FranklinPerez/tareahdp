# Generated by Django 2.2.1 on 2019-07-09 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citasyconsultas', '0042_auto_20190709_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='horCon',
            field=models.ForeignKey(error_messages={'unique_together': 'Esta hora en esta fecha, ya esta ocupada'}, null=True, on_delete=django.db.models.deletion.PROTECT, to='citasyconsultas.Horario'),
        ),
    ]