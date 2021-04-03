from django.db import models

# Create your models here.
class Todo(models.Model):
    title       = models.TextField() 
    description = models.TextField()