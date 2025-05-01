from django.shortcuts import render

# Create your views here.
def enxame(request):
    #print('Teste')
    #return HttpResponse('<body bgcolor-"blue>Alo Mundo!</body>')
    return render(
        request,
        'enxame/index.html'
        #'global/base.html'
    )
