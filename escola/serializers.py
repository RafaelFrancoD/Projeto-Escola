# escola/serializers.py

from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']
        
    def validate(self, dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF deve ter um valor válido'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome': 'O nome deve conter apenas letras'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular': 'O celular deve ter 11 dígitos e conter apenas números, no formato: "XX-XXXXX-XXXX".'})
        return dados

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'celular']  # Apenas os campos desejados

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
        
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    
    class Meta:
        model = Matricula
        fields = ['estudante_nome']
