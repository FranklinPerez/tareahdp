# Generated by Django 2.2.1 on 2019-06-22 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citasyconsultas', '0018_auto_20190622_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fechaNacimiento',
            field=models.DateField(null=True),
        ),
    ]
