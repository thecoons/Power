from __future__ import unicode_literals
# from django.contrib.auth.models import User
from django.db import models

class HearthLog(models.Model):
    brutLog = models.FileField(upload_to='logs/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    filename = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='hearthlog')

    class Meta:
        ordering = ('created',)

# class LogUpload(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     owner = models.ForeignKey('auth.User', related_name='hearthlog')
#     datafile = models.FileField()
