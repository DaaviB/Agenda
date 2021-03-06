from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

def index(request):    
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True,
    )
    
    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    
    return render(request, 'contatos/index.html', context={
        'contatos':contatos,
    })


def details(request, contato_id):
    print(request.path)
    contato = get_object_or_404(Contato, id=contato_id)
    
    if not contato.mostrar:
        raise Http404()
    
    return render(request, 'contatos/detalhes.html', {
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')
    
    if termo is None or not termo:
        messages.error(request, "Preencha o campo de pesquisa!")
        return redirect('index')

    
    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    
    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    
    return render(request, 'contatos/busca.html', context={
        'contatos':contatos,
    })

