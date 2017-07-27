from django.db import models

# Create your models here.
class author(models.Model):
    generes=(('F','Female'),('M','Male'))
    name=models.CharField(max_lenght=50,help_text='Ingrese el nombre del autor: ')
    surname=models.CharField(max_lenght=50,help_text='Ingrese el apellido del author: ')
    bday=models.DateField(help_text='Selecciona la fecha de nacimiento: ')
    genere=models.CharField(max_lenght=50,help_text='Ingrese su genero: ' choices=generes)
    email=models.EmailField(help_text='Escriba su e-mail: ')

class post(models.Model)

    title=models.CharField(max_lenght=50,help_text='Ingrese el titulo de la pelicula: ')
    company=models.CharField(max_lenght=50,help_text='Nombre de la compañia productora: ')
    pubdate=models.DateField(help_text='Fecha de pelicula: ')
    director=models.CharField(max_lenght=50,help_text='Director de la pelicula: ')
    category=models.CharField(max_lenght=50,help_text='Categorias de la pelicula: ')
    sipnosis=models.CharField(max_lenght=50,help_text='Sipnosis de la pelicula: ')
    review=models.CharField(max_lenght=500,help_text='Opinion de la cinta: ')
    stars=models.DecimalField(help_text='Puntuacion que le damos: ')
