from django.shortcuts import render,redirect,get_object_or_404
from .models import *
# from .forms import LivroForms
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class PessoasView(View):
    def get(self, request):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoas.html', {'pessoas': pessoas})


class OcupacoesView(View):
    def get(self, request):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacoes.html', {'ocupacoes': ocupacoes})


class InstituicoesView(View):
    def get(self, request):
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})


class CursosView(View):
    def get(self, request):
        cursos = Curso.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos})


class DisciplinasView(View):
    def get(self, request):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas})


class MatriculasView(View):
    def get(self, request):
        matriculas = Matricula.objects.all()
        return render(request, 'matriculas.html', {'matriculas': matriculas})


class AvaliacoesView(View):
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})


class FrequenciasView(View):
    def get(self, request):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencias.html', {'frequencias': frequencias})


class OcorrenciasView(View):
    def get(self, request):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})


class CidadesView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})


class AreasaberesView(View):
    def get(self, request):
        areasaberes = AreaSaber.objects.all()
        return render(request, 'areasaber.html', {'areasaberes': areasaberes})


class TurnosView(View):
    def get(self, request):
        turnos = Turno.objects.all()
        return render(request, 'turno.html', {'turnos': turnos})


class TurmasView(View):
    def get(self, request):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})


class CursoDisciplinasView(View):
    def get(self, request):
        cursodisciplinas = CursoDisciplina.objects.all()
        return render(request, 'cursodisciplina.html', {'cursodisciplinas': cursodisciplinas})


class AvaliacoesTipoView(View):
    def get(self, request):
        avaliacoestipo = AvaliacaoTipo.objects.all()
        return render(request, 'avaliacoestipo.html', {'avaliacoestipo': avaliacoestipo})
