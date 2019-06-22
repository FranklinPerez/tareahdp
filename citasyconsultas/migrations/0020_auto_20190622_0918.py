# Generated by Django 2.2.1 on 2019-06-22 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citasyconsultas', '0019_auto_20190622_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='servicios',
        ),
        migrations.AddField(
            model_name='consulta',
            name='servicios',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='citasyconsultas.Servicio'),
        ),
    ]