from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.
def home(request):
    dados= ArquivoMidia.objects.all()
    return render(request,"index.html",{'dadosmidia':dados})


def tvscadastradas(request):
    dados= Midia.objects.all()
    return render(request,"tvsLinks.html",{'tvs':dados})

def tv_detail(request, pk):
    tv = ArquivoMidia.objects.filter(midia_id=pk)
    return render(request, 'tv_detail.html', {'tv': tv})

def tv_detail2(request, pk):
    tv = ArquivoMidia.objects.filter(midia_id=pk)
    return render(request, 'tv_detail.html', {'tv': tv})
