# Generated by Django 2.2.1 on 2019-06-21 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citasyconsultas', '0009_merge_20190621_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='codSer',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
