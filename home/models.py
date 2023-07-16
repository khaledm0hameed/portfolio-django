

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(null=True,blank=True,upload_to='photo')
    url = models.CharField(max_length=400)

    def __str__(self):

        return self.name
