from django.db import models
from django.contrib.auth import models as auth_models

class Task(models.Model):

    title = models.CharField(max_length=200)

    author = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)

    opened_at = models.DateTimeField()
    closed_at = models.DateTimeField()

