from django.contrib import admin
from escola.models import Estudante, Curso, Matricula
from .forms import EstudanteForm
class Estudantes(admin.ModelAdmin):
    form = EstudanteForm # Adicionando o formulário personalizado
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular')
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('nome', 'cpf',)
    ordering = ('nome',)
    list_filter = ('data_nascimento', 'cpf')  # Adicionando filtros

admin.site.register(Estudante, Estudantes)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao')
    list_display_links = ('id', 'codigo',)
    search_fields = ('codigo', 'descricao')  # Adicionando busca por descrição
    list_filter = ('nivel',)  # Adicionando filtro por nível

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'estudante', 'curso', 'periodo')
    list_display_links = ('id',)
    search_fields = ('estudante__nome', 'curso__descricao')  # Adicionando busca por nome do estudante e descrição do curso
    list_filter = ('periodo',)  # Adicionando filtro por período

admin.site.register(Matricula, Matriculas)



