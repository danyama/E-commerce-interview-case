from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto,Venda
from .forms import VendaForm, ProdutoForm
from django.utils import timezone
from django.http import HttpResponse

def pagina_inicial(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/pagina_inicial.html', {'produtos':produtos})

def catalogo(request):
    produtos = Produto.objects.exclude(estoque__lte = 0)
    return render(request, 'loja/catalogo.html', {'produtos':produtos})

def contato(request):
    return render(request, 'loja/contato.html')

def adm(request):
    return render(request, 'loja/adm.html')

def produto_new(request):
    form = ProdutoForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            produto = form.save(commit=False)
            produto.save()
            return redirect('catalogo')
    else:
        form = ProdutoForm()
    return render(request, 'loja/produto_new.html', {'form': form})

def lista_edicao(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/lista_edicao.html', {'produtos':produtos})

def produto_edit(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.save()
            return redirect('lista_edicao')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'loja/produto_edit.html', {'form': form})

def produto_detail(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'loja/produto_detail.html', {'produto': produto})

def produto_detail_venda(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'loja/produto_detail_venda.html', {'produto': produto})

def venda_pag(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = VendaForm(request.POST)  
        
        if form.is_valid():
            venda = form.save(commit=False)
            venda.data = timezone.now()
            venda.produto = produto
            venda.idProd()
            venda.vendaTotal()
            venda.save()
            produto.estoque = produto.estoque - venda.quantidade 
            produto.save()
            return redirect('finalizar')
    else:
        form = VendaForm()
    return render(request, 'loja/venda.html', {'form': form})

def finalizar(request):
    venda = Venda.objects.last()
    return render(request, 'loja/finalizar.html', {'venda': venda})