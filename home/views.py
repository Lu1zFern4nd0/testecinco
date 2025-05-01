from django.shortcuts import render
from .models import Comentario

def home(request):
    contexto = {
        'comentarios' : Comentario.objects.all()
    }
    return render(
        request,
        'home/index.html',
        contexto
    )

def gravar_cmt(request):
    novo_comentario = Comentario()
    novo_comentario.nome = request.POST.get('nome')
    novo_comentario.comentario = request.POST.get('cmt')
    novo_comentario.save()

    return home(request)





