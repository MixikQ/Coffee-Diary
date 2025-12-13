from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256, blank=False)
    recipe = models.CharField(max_length=1024)
    comment = models.CharField(max_length=1024)
    by_user = models.PositiveIntegerField()
    date = models.DateTimeField()