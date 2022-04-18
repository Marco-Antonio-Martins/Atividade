from distutils.archive_util import make_zipfile
from email.policy import default
from statistics import mode
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=128)
    email = models.EmailField('E-mail', null=True, blank=True)
    def __str__(self):
        return self.nome

class Autor(Pessoa):
    curriculo = models.CharField('Currículo', max_length=128, null=True)

class PessoaJuridica(Pessoa):
    cnpj = models.CharField('CNPJ', max_length=20)
    razaoSocial = models.CharField('Razão Social', max_length=150)
    def __str__(self):
        return self.razaoSocial

class PessoaFisica(Pessoa):
    cpf = models.CharField('CPF', max_length=20)

class Evento(models.Model):
    nome = models.CharField('Nome', max_length=50, null=True)
    eventoPrincipal = models.TextField('Evento Principal', null=True)
    sigla = models.CharField('Sigla', max_length=10, null=True)
    dataEHoraDeInicio = models.DateTimeField('Data e hora de início', default=None, null=True)
    palavrasChave = models.CharField('Palavras chave', max_length=150, blank=True, null=True)
    logotipo = models.CharField('Logotipo', max_length=50, blank=True, null=True)
    realizador = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)
    cidade = models.CharField('Cidade', max_length=50, blank=True, null=True)
    uf = models.CharField('UF', max_length=20, blank=True, null=True)
    endereco = models.CharField('Endereço', max_length=50, null=True)
    cep = models.CharField('CEP', max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nome

class EventoCientifico(Evento):
    issn = models.CharField('ISSN', max_length=15)

    def __str__(self):
        return self.nome

class ArtigoCientifico(models.Model):
    titulo = models.CharField('Título', max_length=128, null=True)
    autores = models.ManyToManyField(Autor)
    evento = models.ForeignKey(EventoCientifico, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo