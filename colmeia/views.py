from django.shortcuts import render

# Create your views here.
def colmeia(request):
    #print('Teste')
    #return HttpResponse('<body bgcolor-"blue>Alo Mundo!</body>')
    return render(
        request,
        'colmeia/index.html'
        #'global/base.html'
    )
