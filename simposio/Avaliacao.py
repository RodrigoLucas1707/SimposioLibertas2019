from django.db import models
from django.utils import timezone

class Avaliacao(models.Model):
    aprovado = models.BooleanField()
    data_avaliacao = models.DateTimeField(default=timezone.now)
    professor = models.ForeignKey('Professor', on_delete=models.PROTECT)
    submissao = models.ForeignKey('Submissao', on_delete=models.PROTECT)
    aluno = models.ForeignKey('Aluno', on_delete=models.PROTECT)

    def __str__(self):
        return self.aluno.nome+'/'+self.submissao.titulo