from django.contrib.auth.models import User
from django.db import models


class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    nome = models.CharField('Nome', max_length=128)
    data_de_nascimento = models.DateField('Data de Nascimento', blank=True, null=True)
    telefone_celular = models.CharField('Telefone celular ', max_length=15,
                                        help_text='Número do telefone celular no formato(00)00000-0000', null=True,
                                        blank=True)
    telefone_celular = models.CharField('Telefone fixo ', max_length=14,
                                        help_text='Número do telefone celular no formato(00)0000-0000', null=True,
                                        blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)
    funcionario = models.BooleanField(default=False)
    def __str__(self):
        return self.nome

class Orgao(models.Model):
    titulo = models.CharField('titulo', max_length=128, null=True, blank=True)
    descricao = models.CharField('descricao', max_length=128, null=True, blank=True)

class Departamento(models.Model):
    titulo = models.CharField('titulo', max_length=128, null=True, blank=True)
    descricao = models.CharField('descricao', max_length=128, null=True, blank=True)
    id_orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE, null=True, blank=True)

class tramitacao(models.Model):
    data_entrada = models.DateField(auto_now_add=True)
    id_orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE, null=True, blank=True)
    id_departamento_origem = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True, related_name='departamento_origem')
    id_departamento_destino = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True, related_name='departamento_atual')
    data_movimentacao = models.DateField('Novo Prazo', blank=True, null=True)

class Processo(models.Model):
    numero = models.CharField('numero do processo', max_length=15)
    data_criaçao = models.DateField(auto_now_add=True)
    usuario_criador = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True)
    id_interessado = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True, related_name='interessados')
    id_investigado = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True, related_name='investigados')
    id_departamento_criacao = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)

class prazo_processo(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE, null=True, blank=True)
    prazo_original = models.DateField('prazo original', blank=True, null=True)
    pedido_prazo = models.BooleanField(default=False)
    justificativa = models.CharField('justificativa do prazo', max_length=500, null=True, blank=True)
    novo_prazo = models.DateField('Novo Prazo', blank=True, null=True)

class Tipos_documentos(models.Model):
    titulo = models.CharField('titulo', max_length=128, null=True, blank=True)
    descricao = models.CharField('descricao', max_length=128, null=True, blank=True)


class Documentos_processo (models.Model):
    numero = models.CharField('numero', max_length=128, null=True, blank=True)
    tipo_arquivo = models.ForeignKey(Tipos_documentos, on_delete=models.CASCADE, null=True, blank=True)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    arquivo = models.FileField()

class Portaria(models.Model):
    numero = models.CharField('numero', max_length=128, null=True, blank=True)
    documento = models.ForeignKey(Documentos_processo, on_delete=models.CASCADE, null=True, blank=True)

class pedido(models.Model):
    numero = models.CharField('numero', max_length=128, null=True, blank=True)
    documento = models.ForeignKey(Documentos_processo, on_delete=models.CASCADE, null=True, blank=True)

class envio(models.Model):
    numero = models.CharField('numero', max_length=128, null=True, blank=True)
    documento = models.ForeignKey(Documentos_processo, on_delete=models.CASCADE, null=True, blank=True)
    data_envio = models.DateField('prazo original', blank=True, null=True)
    id_departamento_destino = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True,
                                                related_name='departamento_onde_foi_enviado')