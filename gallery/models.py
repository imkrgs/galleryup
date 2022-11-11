from django.db import models

# Create your models here.


class card(models.Model):
    tittle = models.CharField(max_length=100)
    pics = models.FileField(upload_to='media/')
