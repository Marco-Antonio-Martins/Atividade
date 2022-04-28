from distutils.archive_util import make_zipfile
from email.policy import default
from statistics import mode
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=128)
    email = models.EmailField('E-mail')
    def __str__(self):
        return self.nome

class Autor(Pessoa):
    curriculo = models.TextField('Currículo')

class PessoaJuridica(Pessoa):
    cnpj = models.CharField('CNPJ', max_length=20)
    razaoSocial = models.CharField('Razão Social', max_length=150)
    def __str__(self):
        return self.razaoSocial

class PessoaFisica(Pessoa):
    cpf = models.CharField('CPF', max_length=20)

class Evento(models.Model):
    nome = models.CharField('Nome', max_length=150)
    eventoPrincipal = models.TextField('Evento Principal', max_length=150)
    sigla = models.CharField('Sigla', max_length=50)
    dataEHoraDeInicio = models.DateTimeField('Data e hora de início')
    palavrasChave = models.CharField('Palavras chave', max_length=150)
    logotipo = models.CharField(max_length=300)
    realizador = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)
    cidade = models.CharField('Cidade', max_length=100)
    uf = models.CharField('UF', max_length=2)
    endereco = models.CharField('Endereço', max_length=200)
    cep = models.CharField('CEP', max_length=15)

    def __str__(self):
        return self.nome

class EventoCientifico(Evento):
    issn = models.CharField('ISSN', max_length=15)

    def __str__(self):
        return self.nome

class ArtigoCientifico(models.Model):
    titulo = models.CharField('Título', max_length=128)
    autores = models.ManyToManyField(Autor)
    evento = models.ForeignKey(EventoCientifico, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo