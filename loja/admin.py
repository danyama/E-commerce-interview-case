from django.contrib import admin
from .models import Produto,Venda


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display=Produto.DisplayFields


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display=Venda.DisplayFields

