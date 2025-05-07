# ocr/urls.py
from django.urls import path
from .views import OCRImageUpload

urlpatterns = [
    path('upload/', OCRImageUpload.as_view(), name='ocr-upload'),
]
