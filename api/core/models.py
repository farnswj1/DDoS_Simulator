from django.db import models

# Create your models here.
class Data(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Data'
