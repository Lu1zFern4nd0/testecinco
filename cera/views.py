from django.shortcuts import render

# Create your views here.
def cera(request):
    #print('Teste')
    #return HttpResponse('<body bgcolor-"blue>Alo Mundo!</body>')
    return render(
        request,
        'cera/index.html'
        #'global/base.html'
    )
