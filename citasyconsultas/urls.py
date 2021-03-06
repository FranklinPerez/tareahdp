from .ajax import load_Municipio, load_Horario

from django.urls import path, include
from .views import *

app_name = 'citasyconsultas'
urlpatterns=[
	path('index/', index, name='index'),
	#views para medicamento
	path('gestionMedicamento/', ListadoMedicamento.as_view(), name='listado_medicamento'),
	path('crearMedicamento/', crearMedicamento.as_view(), name='crear_medicamento'),
	path('modificarMedicamento/<int:pk>/', modificarMedicamento.as_view(), name='modificar_medicamento'),
	path('eliminarMedicamento/<int:pk>/', eliminarMedicamento.as_view(), name='eliminar_medicamento'),

	# URL's y VIEWS para el control de las citas
	path('nueva_cita/', CrearCita.as_view(), name = 'nueva_cita'),
	path('gestion_cita/', GestionCitas.as_view(), name = 'gestion_cita'),
	path('modificar_cita/<int:pk>/', ModificarCita.as_view(), name = 'modificar_cita'),
	path('cancelar_cita/<int:pk>/', CancelarCita.as_view(), name = 'cancelar_cita'),
	path('confirmar_cancelar/', ConfirmarCancelar, name = 'confirmar_cancelar'),
	path('cobrar/', RealizarCobro, name = 'cobrar'),
	path('citasParaHoy/', citasParaHoy, name='citasParaHoy'),
	
	path('verCita/<int:pk>/', verCita.as_view(), name='verCita'),



	#views para servicio
	path('gestionServicio/', ListadoServicio.as_view(), name='listado_servicio'),
	path('crearServicio/', crearServicio.as_view(), name='crear_servicio'),
	path('modificarServicio/<int:pk>/', modificarServicio.as_view(), name='modificar_servicio'),
	path('eliminarServicio/<int:pk>/', eliminarServicio.as_view(), name='eliminar_servicio'),

	#views para exp
	path('gestionExpediente/', GestionExpediente.as_view(), name='listado_expediente'),
	path('crearExpediente/', crearExpediente.as_view(), name='crear_expediente'),
	path('modificarExpediente/<int:pk>/', modificarExpediente.as_view(), name='modificar_expediente'),

# R ====================================================================================================
    path('ver_expediente/(?P<pk>[0-9]+)/$', DetalleExpediente, name='ver_expediente'),
	path('buscar_exp/', BuscarExpediente, name = 'buscar_exp'),
	# CONSULTAS AJAX PARA EXPEDIENTE Y CITA    =======================
	path('ajax/load_Municipio/', load_Municipio, name='load_Municipio'),
	path('ajax/load_Horario/', load_Horario, name='load_Horario'),
# ======================================================================================================

	#views para consulta
	path('consultasPendientes/', consultasPendientes, name='listado_consulta'),
	path('modificarConsulta/<int:pk>/', modificarConsulta.as_view(), name='modificar_consulta'),
	path('crearConsulta', crearConsulta.as_view(), name='crear_consulta'),

    # VIEWS PARA  CONTROL DE USUARIOS
	path('iniciarSesion', iniciarSesion, name='inicar_sesion'),
	path('autenticarUsuario', autenticarUsuario, name='autenticar_usuario'),
	path('cerrarSesion', cerrarSesion, name='cerrar_sesion'),

	#
	path('gestionMedicamento', ir_a_medicamento, name='ir_a_medicamento'),
	path('gestionServicio', ir_a_servicio, name='ir_a_servicio'),

]

