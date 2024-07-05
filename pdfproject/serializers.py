from rest_framework import serializers
from .models import SplitPDF
from django.utils import timezone

class SplitPDFSerializer(serializers.ModelSerializer):
    original_pdf = serializers.FileField()

    class Meta:
        model = SplitPDF
        fields = [ 'original_pdf', 'split_pdf_location', 'split_date_time']
    def update(self, instance, validated_data):
        '''instance.split_date_time=timezone.now()
        return super().update(instance, validated_data)''' 
        original_pdf = validated_data.pop('original_file')
        document=SplitPDF.objects.update(original_file=original_pdf, **validated_data)
        
        # Split the PDF and save the file paths
        split_files = (instance.original_pdf.path, 'pdfs/split_date_time')
        document.split_files= split_files
        document.save()
      
        return document
    
        