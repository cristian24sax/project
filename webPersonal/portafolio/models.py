from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Portafolio(models.Model):
    title = models.CharField(max_length=200,verbose_name='Titulo')
    description =RichTextField(verbose_name="Contenido")
    image = models.ImageField(default='null',verbose_name="imagen",upload_to='images')
    link=models.URLField(null=True,blank=True,verbose_name="Direccion web")
    public = models.BooleanField(verbose_name="Publicado?")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Creado el ")
    update_at = models.DateTimeField(auto_now=True,verbose_name="Actualizado el ")

    class Meta:
        verbose_name = 'Portafolio'
        verbose_name_plural ='Portafolios'
        ordering =['-created_at']

    def __str__(self):
        return self.title 