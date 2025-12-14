from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256, blank=False)
    recipe = models.CharField(max_length=1024)
    comment = models.CharField(max_length=1024)
    by_user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)