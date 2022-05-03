from django import forms
from django.forms import fields
from .models import Produto, Venda

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('nome_prod', 'imagem', 'preco_unit', 'estoque')


class VendaForm(forms.ModelForm):

    class Meta:
        model = Venda
        fields = ('quantidade', 'cpf', 'email', 'cliente', 'endereco')