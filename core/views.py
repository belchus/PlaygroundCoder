from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from AppCoder.models import Estudiante

class EstudianteListView(ListView):
    model = Estudiante
    template_name = "core/estudiantes.html"


class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = "core/estudiante_detail.html"


class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'email']
    template_name = "core/estudiante_create.html"
    success_url = reverse_lazy('core-Estudiante')


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'email']
    template_name = "core/estudiante_update.html"
    success_url = reverse_lazy('core-Estudiante')


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = "core/estudiante_delete.html"
    success_url = reverse_lazy('core-Estudiante')
