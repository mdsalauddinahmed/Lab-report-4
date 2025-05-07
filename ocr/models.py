# ocr/models.py
from django.db import models

class OCRImage(models.Model):
    image = models.ImageField(upload_to='ocr_images/')
    extracted_text = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
