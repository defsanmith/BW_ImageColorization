from django.db import models

class Image(models.Model):
    bw_img = models.ImageField(upload_to='images/')