from django.db import models
import os
from .color import convert

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    colored = models.ImageField(upload_to='colored/', default='sample.jpeg')

    def save(self, *args, **kwargs):
        self.colored = convert(self.image)

        super(Image, self).save(*args, **kwargs)
