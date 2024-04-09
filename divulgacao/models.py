from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import shutil
import os

# Create your models here.

class Midia(models.Model):
    titulo = models.CharField(max_length=100)

    
    
    class Meta:
        verbose_name = " Cadastrar TV"
        verbose_name_plural = " Cadastrar TVs"

   
    def __str__(self):
       return self.titulo + "  Id Interno: "+str(self.id)




class ArquivoMidia(models.Model):
    midia = models.ForeignKey(Midia, on_delete=models.CASCADE, related_name='arquivos_midia')
    arquivo = models.FileField(upload_to='midia/')
    tipo = models.CharField(max_length=10, choices=[('imagem', 'Imagem'), ('video', 'Vídeo')])
    tempo = models.IntegerField(null=True, blank=True,default=5)  

    def save(self, *args, **kwargs):
        # Se o campo tempo não for None, multiplique por 1000 para converter para milissegundos
        if self.tempo is not None:
            self.tempo *= 1000
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = " Cadastrar Imagem/Video"
        verbose_name_plural = " Cadastrar Imagens/Videos"

    def caminho_completo(self):
        return self.arquivo.url 
    
    def __str__(self):
        return f"{self.midia.titulo} - {self.tipo} - {self.caminho_completo()} - ID Interno : {self.midia_id}  "




@receiver(pre_delete, sender=ArquivoMidia)
def delete_arquivo_midia(sender, instance, **kwargs):
    # Delete the file from storage when the associated ArquivoMidia object is deleted
    if instance.arquivo:
        if os.path.isfile(instance.arquivo.path):
            os.remove(instance.arquivo.path)
        else:
            # If it's a directory, use shutil.rmtree to remove it recursively
            shutil.rmtree(os.path.dirname(instance.arquivo.path))
