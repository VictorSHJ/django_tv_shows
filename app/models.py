from django.db import models
# Create your models here.

class Tvshow(models.Model):
    titulo = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    # libera = models.DateField(null=True)
    descri = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"TV Show: {self.titulo}, Network:{self.descri}"
    def __str__(self):
        return f"tv show: {self.titulo}, network:{self.descri}"