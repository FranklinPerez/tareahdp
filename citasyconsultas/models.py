from .validators import valid_Nombres, valid_Apellidos, valid_Telefono
from django.core.exceptions import ValidationError

from django.db import models
from datetime import *
from django.utils import timezone



class Horario(models.Model):
	hora = models.CharField(max_length = 10)

	def __str__(self):
		return self.hora

# Modelo de los Servicios
class Servicio (models.Model):

	codSer = models.IntegerField(primary_key = True)
	nomSer = models.CharField(max_length = 200) # Nombre del servicio
	precio = models.DecimalField(max_digits = 10, decimal_places = 2)
	duraci = models.CharField(max_length = 10)# Duracion PROMEDIO del servicio en minutos

	def __str__(self):
		return self.nomSer
	
	class Meta:
		ordering = ('nomSer',)

class Departamento(models.Model):
	numDep = models.IntegerField(primary_key = True) 
	nomDep = models.CharField(max_length = 100, help_text = "Ingrese un departamento")
	def __str__(self):
		return self.nomDep

	class Meta:
		ordering = ('nomDep',)

class Municipio(models.Model):
	numMunicipio = models.IntegerField(primary_key = True)
	nomMunicipio = models.CharField(max_length = 100, help_text = "Ingrese un municipio")
	departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
	def __str__(self):
		return self.nomMunicipio	

	class Meta:
		ordering = ('nomMunicipio',)

class Paciente(models.Model):
	numExpediente = models.IntegerField(primary_key = True)
	nomPaciente = models.CharField(max_length = 200, help_text = "Ingrese el nombre del paciente", validators = [valid_Nombres])
	apelPaciente = models.CharField(max_length = 200, help_text = "Ingrese el apellido del paciente", validators = [valid_Apellidos])
	fechaNacimiento = models.DateField(null=True, blank=True)
	emailPaciente = models.CharField(max_length = 200, help_text = "Ingrese eMail del paciente")
	depResidencia = models.ForeignKey(Departamento, on_delete=models.PROTECT, default = '10')
	munResidencia = models.ForeignKey(Municipio, on_delete = models.PROTECT, default = '15')
	telefono = models.CharField(max_length = 8, help_text = "Solo numeros", validators=[valid_Telefono])
	def __str__(self):
		return self.apelPaciente + ", " + self.nomPaciente

	class  Meta:
		unique_together = ['telefono',]


# Modelo de laas citas.
class Cita (models.Model):
	numCit = models.IntegerField(primary_key = True, help_text = "Numero de cita del dia", error_messages={'unique':"Ya existe una Cita con este numero"})# Numero de cita del dia
	pacien = models.ForeignKey('Paciente', on_delete = models.PROTECT, null=True)
	fecCon = models.DateField(null=True, verbose_name="Fecha de Cita")# Fecha de la consulta
	horCon = models.ForeignKey(Horario, null=True, on_delete=models.PROTECT, verbose_name="Hora de Cita")
	servic = models.ForeignKey(Servicio,on_delete = models.PROTECT, null=True)
	estado = models.IntegerField(default=0, null=True, help_text = "Activa (0), Completada (1)") #  Pendiente = 0 ,  Completado = 1
	fecCre = models.DateField(auto_now_add = True)# fecha de creacion
	
	def __str__(self):
		return self.numCit

	class Meta:
		ordering = ('numCit',)
		unique_together =['fecCon', 'horCon']
    

	def unique_error_message(self, model_class, unique_check):
		if len(unique_check) != 1:
			return 'Esta hora en esta fecha ya esta ocupada, seleccione otra hora y/o fecha'

# Create your models here.
class Medicamento(models.Model):
	codMedicamento=models.IntegerField(help_text="Ingrese el codigo del Medicamento",primary_key = True)
	nomMedicamento=models.CharField(max_length=200,help_text="Ingrese el nombre del Medicamento")
	def __str__(self):
		return self.nomMedicamento

class Medico(models.Model):
	codMedico=models.IntegerField(help_text="Ingrese el codigo del Medico",primary_key = True)
	nomMedico=models.CharField(max_length=200,help_text="Ingrese el nombre del Medico")
	usuario=models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
	def __str__(self):
		return self.nomMedico

class Secretaria(models.Model):
	codSec=models.IntegerField(help_text="Ingrese el codigo de la Secretaria",primary_key = True)
	nomSec=models.CharField(max_length=200,help_text="Ingrese el nombre de la Secretaria")
	usuario=models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
	def __str__(self):
		return self.nomSec

class Usuario(models.Model):
	codUsu=models.CharField(max_length=10,help_text="Ingrese el Usuario, maximo 10 caracteres",primary_key = True)
	pasUsu=models.CharField(max_length=20,help_text="Ingrese contraseña, maximo 20 caracteres")

	TIPO_USUARIO= (
		('s','Secretaria'),
		('m', 'Medico'),		
		)

	tipo_usuario= models.CharField(
        max_length=1,
        choices=TIPO_USUARIO,
        blank=True,
        default='s',
        help_text='Tipo de usuario en el sistema')

	def __str__(self):
		 return '{0}, {1},{2}'.format(self.codUsu, self.pasUsu, self.tipo_usuario)


class Consulta(models.Model):
	codCon=models.IntegerField(primary_key = True)
	diagnostico=models.CharField(max_length=500,help_text="Ingrese el diagnostico", null=True, blank=True)	
	dosis=models.CharField(max_length=500,help_text="Ingrese la dosis", null=True, blank=True)
	paciente = models.ForeignKey('Paciente', help_text="Seleccione el paciente",on_delete=models.SET_NULL, null=True)
	#medico=models.ForeignKey('Medico', on_delete=models.SET_NULL, null=True)
	fecConHoy=models.DateField(default=datetime.now().date())
	medicamentos=models.ManyToManyField(Medicamento, null=True, blank=True)
	servicios=models.ForeignKey('Servicio', blank=True, on_delete=models.SET_NULL, null=True)
	
	Estado_Consulta= (
		('f','Finalizada'),
		('p', 'Pendiente'),		
		)

	estado= models.CharField(
        max_length=1,
        choices=Estado_Consulta,
        blank=True,
        default='p')


	def __str__(self):
		return self.dosis




