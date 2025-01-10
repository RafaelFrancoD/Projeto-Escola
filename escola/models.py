from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator

def validar_cpf(valor):
    if len(valor) != 11 or not valor.isdigit():
     raise ValidationError('O CPF deve ter 11 dígitos e conter apenas números.')

def validar_celular(valor):
    if len(valor) != 11 or not valor.isdigit():
        raise ValidationError('O número de celular deve ter 14 dígitos e conter apenas números, no formato: "XX-XXXXX-XXXX".')
class Estudante(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length = 11, validators=[validar_cpf])
    data_nascimento = models.DateField()
    celular = models.CharField(max_length = 11, validators=[validar_celular])

    def __str__(self):
        return self.nome
    

class Curso(models.Model):
    NIVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    ) 
    codigo = models.CharField(max_length = 10, unique = True, validators =[MinLengthValidator(3)])
    descricao = models.CharField(max_length = 100, blank = False)
    nivel = models.CharField(max_length = 1, choices = NIVEL, blank = False, null = False, default = 'B')

    def __str__(self):
        return self.codigo   
    
class Matricula(models.Model):
    PERIODO = (
        ('M','Matutino'),
        ('V','Vespertino'),
        ('N','Noturno'),
    )
    estudante = models.ForeignKey(Estudante,on_delete = models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete = models.CASCADE)
    periodo = models.CharField(max_length = 1, choices = PERIODO, blank = False, null = False, default = 'M')  
