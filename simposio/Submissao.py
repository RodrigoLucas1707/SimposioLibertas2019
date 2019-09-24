from django.db import models
from django.utils import timezone

class Submissao(models.Model):
    data_envio = models.DateTimeField(default=timezone.now)
    titulo = models.CharField(max_length=50)
    resumo = models.TextField()
    palavras_chave = models.TextField()
    data_aceite = models.DateTimeField(default=timezone.now)
    data_aprovacao = models.DateTimeField(default=timezone.now)
    area = models.ForeignKey('Area', on_delete=models.PROTECT)
    status = models.ForeignKey('Status', on_delete=models.PROTECT)
    orientador = models.ForeignKey('Professor', on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

