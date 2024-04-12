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
    return render(request, 'teste.html', {'tv': tv})

def tv_webm(request, pk):
    tv = ArquivoMidia.objects.filter(midia_id=pk)
    return render(request, 'tvwebm.html', {'tv': tv})

def tv_mp4(request, pk):
    tv = ArquivoMidia.objects.filter(midia_id=pk)
    return render(request, 'tvmp4.html', {'tv': tv})

def tv_mov(request, pk):
    tv = ArquivoMidia.objects.filter(midia_id=pk)
    return render(request, 'tvmov.html', {'tv': tv})

def tv_mpeg(request, pk):
    tv = ArquivoMidia.objects.filter(midia_id=pk)
    return render(request, 'tvmpeg.html', {'tv': tv})

def tv_mkv(request, pk):
    tv = ArquivoMidia.objects.filter(midia_id=pk)
    return render(request, 'tvmkv.html', {'tv': tv})