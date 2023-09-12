from django.db import models

class Chiste(models.Model):
    texto = models.TextField()

    def __str__(self):
        return self.texto