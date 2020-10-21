from django.db import models

# Create your models here.

class SmzdmResult(models.Model):
    title = models.CharField(max_length = 200)
    comment = models.CharField(max_length = 1000)
    sentiment = models.FloatField()
    