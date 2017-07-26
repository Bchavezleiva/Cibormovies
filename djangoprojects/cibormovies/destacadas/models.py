from django.db import models

# Create your models here.
class post(models.Model):
    """
    Almacena las publicaciones realizadas por el equipo administrativo
    """
    title=models.CharField(max_lenght=50,help_text='Ingrese el titulo de la pelicula')
    company=models.CharField(max_lenght=50,help_text='Nombre de la compañia productora')
    pubdate=models.DateField(max_lenght=50,help_text='Fecha de pelicula')
    director=models.CharField(max_lenght=50,help_text='Director de la pelicula')
    category=models.CharField(max_lenght=50,help_text='Categorias de la pelicula')
    review=models.CharField(max_lenght=500,help_text='Opinion de la cinta')

class comments(models.Model):
    post=models.ForeignKey(post,help_text='Seleccione la publicacion')
