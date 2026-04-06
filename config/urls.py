from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoa/', PessoasView.as_view(), name='pessoa'),
    path('ocupacoes/', OcupacoesView.as_view(), name='ocupacoes'),
    path('instituicao/', InstituicoesView.as_view(), name='instituicao'),
    path('areasaber/', AreasaberesView.as_view(), name='area_saber'),
    path('cursos/', CursosView.as_view(), name='curso'),
    path('turma/', TurmasView.as_view(), name='turma'),
    path('disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
    path('matriculas/', MatriculasView.as_view(), name='matriculas'),
    path('avaliacoes/', AvaliacoesView.as_view(), name='avaliacoes'),
    path('frequencias/', FrequenciasView.as_view(), name='frequencias'),
    path('turnos/', TurnosView.as_view(), name='turnos'),
    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('ocorrencias/', OcorrenciasView.as_view(), name='ocorrencias'),
    path('cursodisciplina/', CursoDisciplinasView.as_view(), name='cursodisciplina'),
    path('avaliacoestipo/', AvaliacoesTipoView.as_view(), name='avaliacoestipo'),
]