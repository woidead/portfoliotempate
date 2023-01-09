from django.db import models

# Create your models here.
class Skill(models.Model):
    title = models.CharField(max_length=255, help_text="Твои хард скиллы",verbose_name='новый навык')

class Message(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='почта')
    text = models.TextField(verbose_name='сообщение')
 
class Project(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField()
    link = models.URLField()
    image = models.ImageField(upload_to='static')