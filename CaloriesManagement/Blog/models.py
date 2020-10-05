from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.


class food(models.Model):
    
    name = models.CharField(max_length=50,verbose_name='Nombre')
    calories = models.IntegerField(verbose_name="Calorias")
    

     
    class Meta:
        verbose_name='Alimento'
        verbose_name_plural='Alimentos'
        
    def __str__(self):
        return self.name

class hora(models.Model):
    hora_dia = models.CharField(max_length=20,verbose_name='Hora Del Dia')

    class Meta:
        verbose_name='Hora del dia'
    
    def __str__(self):
        return self.hora_dia
        
        
    
class meal(models.Model):
    choices=[
        ('Lunes','Lunes'),
        ('Martes','Martes'),
        ('Miercoles','Miercoles'),
        ('Jueves','Jueves'),
        ('Viernes','Viernes'),
        ('Sabado','Sabado'),
        ('Domingo','Domingo')]
    days = models.CharField(choices=choices,max_length=10,default='Lunes')
    hora = models.ForeignKey(hora,on_delete=models.CASCADE,default='')
    food = models.ForeignKey(food,on_delete=models.CASCADE,default='')
    user = models.ForeignKey(User,editable=False,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='Registros'
        
    def __str__(self):
        return self.days



