
from django.urls import path
from core import views

urlpatterns = [
    path('estudiantes/', views.EstudianteListView.as_view(), name="core-Estudiante"),
    path('estudiantes/<int:pk>/', views.EstudianteDetailView.as_view(), name="core-Estudiante-detail"),
    path('estudiantes/create/', views.EstudianteCreateView.as_view(), name="core-Estudiante-create"),
    path('estudiantes/update/<int:pk>/', views.EstudianteUpdateView.as_view(), name="core-Estudiante-update"),
    path('estudiantes/delete/<int:pk>/', views.EstudianteDeleteView.as_view(), name="core-Estudiante-delete"),
]
