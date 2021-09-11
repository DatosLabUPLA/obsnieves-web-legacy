from django.db import models
from django.utils.html import format_html
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class New(models.Model):
    FEATURED_NO = 0
    FEATURED_YES = 1
    FEATURED_CHOICE = [
        (FEATURED_NO, 'No destacada'),
        (FEATURED_YES, 'Destacada'),
    ]

    headline = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(unique=True, max_length=255, default='', verbose_name='Slug')
    lead = models.TextField(max_length=500, verbose_name='Bajada')
    body = RichTextUploadingField(blank=True, verbose_name='Cuerpo')
    link_source = models.URLField(max_length=500, verbose_name='URL de la fuente')
    link_image = models.URLField(max_length=300, blank=True, verbose_name='URL de la imagen')
    
    date = models.DateField(verbose_name='Fecha de la noticia')
    id_origin = models.ForeignKey('Origin', default=None, on_delete=models.PROTECT, verbose_name='Origen')
    featured = models.IntegerField(choices=FEATURED_CHOICE, default=FEATURED_NO, verbose_name='Noticia Destacada')

    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='modificado')

    class Meta:
        verbose_name = 'noticia'
        verbose_name_plural = 'noticias'
        ordering = ['-date']
    
    def __str__(self):
        return self.headline

    


class Origin(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre del origen')
    short_name = models.CharField(max_length=10, verbose_name='Nombre corto del origen')
    link = models.URLField(max_length=300, verbose_name='URL del origen')
    color_hex = models.CharField(max_length=7, default="#ffffff", verbose_name='Color del origen')

    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='modificado')

    class Meta:
        verbose_name = 'fuente'
        verbose_name_plural = 'fuentes'
        ordering = ['-name']
    
    def __str__(self):
        return self.name


