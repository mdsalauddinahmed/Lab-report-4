# ocr/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import OCRImage
from .serializers import OCRImageSerializer
import pytesseract
from PIL import Image

class OCRImageUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = OCRImageSerializer(data=request.data)
        if serializer.is_valid():
            ocr_image = serializer.save()

            # Run OCR using pytesseract
            image_path = ocr_image.image.path
            image = Image.open(image_path)
            extracted_text = pytesseract.image_to_string(image)

            # Save extracted text
            ocr_image.extracted_text = extracted_text
            ocr_image.save()

            return Response(OCRImageSerializer(ocr_image).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
