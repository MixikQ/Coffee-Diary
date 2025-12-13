from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length = 32, blank=False)
    
class Post(models.Model):
    title = models.CharField(max_length = 256, blank=False)
    recipe = models.CharField(max_length = 1024)
    comment = models.CharField(max_length = 1024)
    by_user = models.PositiveIntegerField()
    date = models.DateTimeField()
