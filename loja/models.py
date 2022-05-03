from django.conf import settings
from django.db import models
from django.utils import timezone
from cpf_field.models import CPFField

class Produto(models.Model):
    nome_prod = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to="media")
    preco_unit = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    DisplayFields = ['nome_prod', 'imagem', 'preco_unit', 'estoque', 'pk']
    def atualizarEstoque(self, saida):
        self.estoque = self.estoque - saida
        return self.estoque

    def __str__(self):
        return self.nome_prod


class Venda(models.Model):
    email = models.EmailField(max_length=254)
    cliente =  models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    data = models.DateTimeField(default=timezone.now)
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    cpf = CPFField('cpf')
    DisplayFields = ['email', 'cliente', 'endereco', 'data', 'quantidade', 'cpf', 'idProd', 'produto', 'vendaTotal']
    
    def idProd(self):
        id_produto = self.produto.pk
        return id_produto

    def vendaTotal(self):
        total = self.quantidade * self.produto.preco_unit
        return total

    
