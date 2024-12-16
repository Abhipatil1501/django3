from django.db import models

class KannadaText(models.Model):
    kannada_text = models.CharField(max_length=255)

# Create your models here.
