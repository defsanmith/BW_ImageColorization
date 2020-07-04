from django import forms
from django.core.files import File
from .models import Image
import numpy as np
import cv2
from .color import convert

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
