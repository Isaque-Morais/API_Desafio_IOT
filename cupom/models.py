from django.db import models

class Cupom(models.Model):
    numero_cupom = models.CharField(max_length=8)
    cnpj = models.CharField(max_length=14)
    cpf_doador = models.CharField(max_length=11)
    valor_compra = models.CharField(max_length=8)
    data = models.DateField()
    entidade_doacao =models.CharField(max_length=20)
    
    def __str__(self):
        return self.numero_cupom

class ModeloNota(models.Model):
    TIPOS = (
        ('C', 'Cumpom Fiscal'),
        ('N', 'Nota Fiscal'),
    )
    codigo_nota = models.CharField(max_length=8)
    descricao = models.CharField(max_length=100)
    tipos = models.CharField(max_length=1, choices=TIPOS, blank=False, null=False, default='C')
    
    def __str__(self):
        return self.descricao
    