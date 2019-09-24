from django.contrib import admin

from .Area import Area
admin.site.register(Area)

from .Aluno import Aluno
admin.site.register(Aluno)

from .Professor import Professor
admin.site.register(Professor)

from .Status import Status
admin.site.register(Status)

from .Avaliacao import Avaliacao
admin.site.register(Avaliacao)

from .Submissao import Submissao
admin.site.register(Submissao)

from .Autores import Autores
admin.site.register(Autores)


