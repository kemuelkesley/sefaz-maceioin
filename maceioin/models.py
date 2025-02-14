from django.db import models

# Create your models here.


class Servidor(models.Model):
    SETORES = [
        ('Contabilidade', 'Contabilidade'),
        ('Financeiro', 'Financeiro'),
        ('Atendimento', 'Atendimento'),
        ('Orçamento', 'Orçamento'),
        ('TI', 'TI'),
    ]

    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=20, choices=SETORES)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome