from django.shortcuts import render

# Create your views here.
def curiosidade(request):
    #print('Teste')
    #return HttpResponse('<body bgcolor-"blue>Alo Mundo!</body>')
    return render(
        request,
        'curiosidade/index.html'
        #'global/base.html'
    )
