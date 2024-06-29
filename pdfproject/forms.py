from .models import SplitPDF
from django import forms


class SplitPDF(forms.ModelForm):
    
   original_pdf = forms.FileField(localize='pdf_split_parts/')
   split_pdf_name = forms.CharField(max_length=255, )
   split_pdf_location = forms.CharField(max_length=255) # For storing custom split PDF name
   split_date_time= forms.DateTimeField(required=True)

    
def __str__(self):
        return f"{self.original_pdf.name} - Part -{self.id} - Part{self.split_date_time}-Part{self.split_pdf_location}" 
    
class Meta:
        model = SplitPDF
        fields = '__all__'