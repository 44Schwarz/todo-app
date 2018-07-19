from django.db import models


# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=50, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.name if self.name else self.text[:50]
