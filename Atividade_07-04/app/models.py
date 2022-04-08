from distutils.archive_util import make_zipfile
from email.policy import default
from statistics import mode
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=128)
    email = models.EmailField('E-mail', null=True, blank=True)
    def __str__(self):
        return self.nome

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
     
'''class PessoaJuridica(Pessoa):
    cnpj = ""
    razaoSocial = ""

class PessoaFisica(Pessoa):
    cpf = ""

class Autor(Pessoa):
    curriculo = ""
    artigos = []

class ArtigoCientifico:
    titulo = ""
    autores = []
    evento = EventoCientifico()
'''


'''class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    nome = models.CharField('Nome', max_length=128)
    data_de_nascimento = models.DateField('Data de nascimento', blank=True, null=True)
    telefone_celular = models.CharField('Telefone celular', max_length=15, help_text='Número do telefone celular no formato (99) 99999-9999', null=True, blank=True)
    telefone_fixo = models.CharField('Telefone fixo', max_length=14, help_text='Número do telefone fixo no formato (99) 9999-9999', null=True, blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)
    def __str__(self):
        return self.nome'''