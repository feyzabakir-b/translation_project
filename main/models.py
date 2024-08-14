from django.db import models
from unidecode import unidecode

class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    normalized_name = models.CharField(max_length=100, editable=False)

    def save(self, *args, **kwargs):
        self.normalized_name = unidecode(self.name.lower())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name