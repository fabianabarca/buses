from django.db import models 

# Create your models here.

class Noticia(models.Model):
   titulo = models.CharField(
      max_length=64,
      help_text='Título de la noticia')
   fecha_publicacion = models.DateField(
      help_text="Fecha de publicación")
   descripcion_corta = models.CharField(
      max_length=500,
      help_text="Descripción corta de la noticia")
   descripcion_larga = models.TextField(
      max_length=50000,
      help_text="Descripción completa de la noticia")
   imagen_noticia = models.ImageField(
      upload_to='noticias',
      blank=True)
   fecha_expiracion = models.DateField(
      help_text="Fecha de expiración de publicación")

   def __str__(self):
      return self.titulo

class Aviso(models.Model):
   titulo=models.CharField(
      max_length=30,
      help_text='Título del aviso')
   fecha_publicacion=models.DateField(
      blank=True,
      help_text="Fecha de publicación")
   descripcion=models.CharField(
      max_length=500,
      help_text="Descripción aviso")
   fecha_expiracion=models.DateField(
      help_text="Fecha de expiracion de publicación")
   urgencia=models.IntegerField(
      help_text='Urgencia del aviso')

   def __str__(self):
      return '%s. Fecha: %s. Descripción: %s' %(self.titulo, self.fecha_publicacion, self.descripcion)