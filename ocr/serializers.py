# ocr/serializers.py
from rest_framework import serializers
from .models import OCRImage

class OCRImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OCRImage
        fields = ['id', 'image', 'extracted_text', 'uploaded_at']
        read_only_fields = ['extracted_text', 'uploaded_at']
