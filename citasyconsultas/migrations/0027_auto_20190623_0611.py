# Generated by Django 2.2.1 on 2019-06-23 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citasyconsultas', '0026_auto_20190623_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='numCit',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
