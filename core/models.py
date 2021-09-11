from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    id_position = models.ForeignKey('Position', default=None, on_delete=models.PROTECT, verbose_name='Cargo')
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(null=True, blank=True, upload_to='images/team/', verbose_name='Imagen')
    index = models.PositiveSmallIntegerField(default=0, verbose_name='Indice', help_text="Este campo se utiliza para dar orden de preferencia de aparición. Evitar modificar.")

    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='modificado')

    class Meta:
        verbose_name = 'miembro del equipo'
        verbose_name_plural = 'miembros del equipo'
        ordering = ['-created']
    
    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre del cargo')
    description = models.CharField(null=True, blank=True, max_length=200, verbose_name='Descripción')

    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='modificado')

    class Meta:
        verbose_name = 'cargo'
        verbose_name_plural = 'cargos'
        ordering = ['-created']
    
    def __str__(self):
        return self.name
