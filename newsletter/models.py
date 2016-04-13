from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(blank=False, null=True, max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __unicode__(self):
        return self.email

