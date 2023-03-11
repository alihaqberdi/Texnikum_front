from django.db import models

class Clinic(models.Model):
    name = models.CharField(verbose_name="Poliklinika nomi", max_length=255)

    def __str__(self):
        return self.name
