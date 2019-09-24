from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=20)
    usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)

    def __str__(self):
        return self.nome