from django.db import models

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
    tempo = models.DurationField(null=True, blank=True)

    class Meta:
        verbose_name = " Cadastrar Imagem/Video"
        verbose_name_plural = " Cadastrar Imagens/Videos"

    def caminho_completo(self):
        return self.arquivo.url 
    
    def __str__(self):
        return f"{self.midia.titulo} - {self.tipo} - {self.caminho_completo()} - ID Interno : {self.midia_id}  "





