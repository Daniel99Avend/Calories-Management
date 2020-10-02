from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.

class kind_food(models.model):
    title = models.CharField(max_length=10,verbose_name='Titulo')
    description = models.TextField(max_lenght=50,verbose_name='Descripcion')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='creado el')

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.title


class food(models.model):
    name = models.CharField(max_length=10,verbose_name='Nombre')
    calories = models.IntegerField(verbose_name="Calorias")
    category = models.ManyToManyField(kind_food, verbose_name=("Categoria"))

    class Meta:
        verbose_name='Alimento'
        verbose_name_plural='Alimentos'
        
    def __str__(self):
        return self.name

class meal(models.model):
    choices=[
        'Lunes',
        'Martes',
        'Miercoles',
        'Jueves',
        'Viernes',
        'Sabado',
        'Domingo']
    day = models.CharField(choices=choices,default='Lunes')
    food = models.ManyToManyField(food,verbose_name='comidas')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Menu'
        
    def __str__(self):
        return self.day




