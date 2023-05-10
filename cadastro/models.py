from django.db import models


class ResponsavelFamiliar(models.Model):
    nome = models.CharField(max_length=30)
    def __str__(self):
        return self.nome


class MembroFamiliar(models.Model):
    nome = models.CharField(max_length=30)
    responsavel_familiar = models.ForeignKey(ResponsavelFamiliar, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome