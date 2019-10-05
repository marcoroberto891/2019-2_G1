from django.contrib import admin
from . import models

@admin.register(models.Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Processo)
class ProcessoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Orgao)
class OrgaoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Documentos_processo)
class Documentos_processoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.prazo_processo)
class prazo_processoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Tipos_documentos)
class Tipos_documentosAdmin(admin.ModelAdmin):
    pass