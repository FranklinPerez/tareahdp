
from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from datetime import *
from .models import *
from .forms import *

def index(request):   

    return render(
        request,
        'base/base.html',
        context={},
    )
# CITA Y SU CRUD==========================================================================
# Vista de la creacion de cita
class CrearCita(CreateView):
	template_name = 'citasyconsultas/cita_form.html'
	form_class= NuevaCitaForm
	success_url = reverse_lazy('citasyconsultas:gestion_cita')
    

class GestionCitas(ListView):
	model = Cita
	template_name = 'citasyconsultas/gestionCitas.html'
	context_object_name = 'GestionCitas'


class ModificarCita(UpdateView):
    template_name = 'citasyconsultas/cita_form.html'
    model = Cita
    form_class = NuevaCitaForm
    success_url = reverse_lazy('citasyconsultas:gestion_cita')
    

class EliminarCita(DeleteView):
    template_name = 'citasyconsultas/eliminarCita.html'
    model = Cita
    success_url = reverse_lazy('citasyconsultas:gestion_cita')

#==========================================================================




#modelos de Medicamento
class ListadoMedicamento(ListView):
    model = Medicamento
    template_name = 'citasyconsultas/gestionMedicamento.html'
    context_object_name = 'medicamentos'

class crearMedicamento(CreateView):
    template_name = 'citasyconsultas/crearMedicamento.html'
    form_class = MedicamentoForm
    success_url = reverse_lazy('citasyconsultas:listado_medicamento')

class modificarMedicamento(UpdateView):
    model = Medicamento
    template_name = 'citasyconsultas/crearMedicamento.html'
    form_class = MedicamentoForm
    success_url = reverse_lazy('citasyconsultas:listado_medicamento')

class eliminarMedicamento(DeleteView):
    model = Medicamento
    template_name='citasyconsultas/eliminarMedicamento.html'
    success_url = reverse_lazy('citasyconsultas:listado_medicamento')

#modelos de Servicio
class ListadoServicio(ListView):
    model = Servicio
    template_name = 'citasyconsultas/gestionServicio.html'
    context_object_name = 'servicios'

class crearServicio(CreateView):
    template_name = 'citasyconsultas/crearServicio.html'
    form_class = ServicioForm
    success_url = reverse_lazy('citasyconsultas:listado_servicio')

class modificarServicio(UpdateView):
    model = Servicio
    template_name = 'citasyconsultas/crearServicio.html'
    form_class = ServicioForm
    success_url = reverse_lazy('citasyconsultas:listado_servicio')

class eliminarServicio(DeleteView):
    model = Servicio
    template_name='citasyconsultas/eliminarServicio.html'
    success_url = reverse_lazy('citasyconsultas:listado_servicio')




class BuscarExpediente(ListView):
    model = Paciente
    template_name = 'citasyconsultas/gestionExpediente.html'
    context_object_name = 'expedientes'

class crearExpediente(CreateView):
    template_name = 'citasyconsultas/crearExpediente.html'
    form_class = ExpedienteForm
    success_url = reverse_lazy('citasyconsultas:listado_expediente')

class modificarExpediente(UpdateView):
    model = Paciente
    template_name = 'citasyconsultas/crearExpediente.html'
    form_class = ExpedienteForm
    success_url = reverse_lazy('citasyconsultas:listado_expediente')



def consultasPendientes(request):
    fechahoy=datetime.now().date()
    consultas=Consulta.objects.filter(estado='p').filter(fecConHoy__contains=fechahoy)            
    return render(request, 'citasyconsultas/consultasPendientes.html',context={'consultas':consultas})

class modificarConsulta(UpdateView):
    model = Consulta
    template_name = 'citasyconsultas/modificarConsulta.html'
    form_class = ConsultaForm
    success_url = reverse_lazy('citasyconsultas:listado_consulta')

class crearConsulta(CreateView):   
    template_name = "citasyconsultas/crearConsulta.html"
    form_class = nuevaConsultaForm
    success_url = reverse_lazy('citasyconsultas:gestion_servicio')


   
   
        
              
        