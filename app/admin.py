from django.contrib import admin
from .models import *

# class LivroInline(admin.TabularInline):
#     model = Livro
#     extra = 1 

# class AutorAdmin(admin.ModelAdmin):
#     list_display = ('nome',)
#     search_fields = ('nome',)
#     inlines = [LivroInline]

admin.site.register(Cidade)
# admin.site.register(Autor,AutorAdmin)
admin.site.register(Pessoa)
admin.site.register(Ocupacao)
admin.site.register(InstituicaoEnsino)
admin.site.register(AreaSaber)
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turno)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
admin.site.register(AvaliacaoTipo)



