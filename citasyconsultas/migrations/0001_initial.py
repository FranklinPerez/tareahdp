
# Generated by Django 2.2.1 on 2019-06-17 05:31

from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(

            name='Cita',
            fields=[
                ('numCit', models.IntegerField(primary_key=True, serialize=False)),
                ('nomPac', models.CharField(max_length=255)),
                ('apePac', models.CharField(max_length=255)),
                ('telPac', models.IntegerField(unique=True)),
                ('fecCon', models.DateField()),
                ('fecCre', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('numCit',),
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('codSer', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nomSer', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=3)),
                ('duraci', models.DurationField()),
            ],
            options={
                'ordering': ('codSer',),
            },
        ),
        migrations.CreateModel(
            name='CitaServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='citasyconsultas.Cita')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='citasyconsultas.Servicio')),
        
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codMedicamento', models.CharField(help_text='Ingrese el codigo del Medicamento', max_length=10)),
                ('nomMededicamento', models.CharField(help_text='Ingrese el nombre del Medicamento', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codMedico', models.CharField(help_text='Ingrese el codigo del Medico', max_length=10)),
                ('nomMedico', models.CharField(help_text='Ingrese el nombre del Medico', max_length=200)),

            ],
        ),
    ]
