from django.db import models

# Create your models here.
class Cuenta(models.Model):
    id=models.AutoField(primary_key=True)
    correo=models.EmailField()
    contra=models.CharField(max_length=100)