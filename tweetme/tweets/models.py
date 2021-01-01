from django.db import models


class Tweet(models.Model):
    content = models.CharField(max_length=200, blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True)
