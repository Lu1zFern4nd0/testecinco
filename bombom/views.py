from django.shortcuts import render

# Create your views here.
def bombom(request):
    #print('Teste')
    #return HttpResponse('<body bgcolor-"blue>Alo Mundo!</body>')
    return render(
        request,
        'bombom/index.html'
        #'global/base.html'
    )
