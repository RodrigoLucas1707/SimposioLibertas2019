from django.db import models

class Autores(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete=models.PROTECT)
    professor = models.ForeignKey('Professor', on_delete=models.PROTECT)
    submissao = models.ForeignKey('Submissao', on_delete=models.PROTECT)

    def __str__(self):
        return self.submissao.titulo+'/'+(self.aluno.nome)+'/'+(self.professor.nome)