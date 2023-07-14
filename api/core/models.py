from django.db import models

# Create your models here.
class Data(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}: {self.username} ({self.password})'

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Data'
