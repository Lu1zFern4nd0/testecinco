from django.shortcuts import render

# Create your views here.
def contato(request):
    #print('Teste')
    #return HttpResponse('<body bgcolor-"blue>Alo Mundo!</body>')
    return render(
        request,
        'contato/index.html'
        #'global/base.html'
    )
