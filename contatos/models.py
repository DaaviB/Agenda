from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=100)
    
    
    def __str__(self) -> str:
        return self.nome
    
    
class Contato(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    telefone = models.CharField('Telefone', max_length=40)
    email = models.CharField('Email', max_length=60)
    data_criacao = models.DateTimeField('Data de Criação', default=timezone.now)
    descricao = models.TextField('Descrição', blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=DO_NOTHING, verbose_name='Categoria')
    mostrar = models.BooleanField('Mostrar', default=True)
    
    
    def __str__(self) -> str:
        return self.nome 