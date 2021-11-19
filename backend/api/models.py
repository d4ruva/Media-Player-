from django.db import models

# Create your models here.

class songs(models.Model):
    name = models.CharField(max_length=30)
    songfile = models.FileField(upload_to="songs")
    aurthor = models.CharField(max_length=30)

    def __str__(self):
        return self.name