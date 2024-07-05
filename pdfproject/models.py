from django.db import models



# Create your models here.
class SplitPDF(models.Model):
   original_pdf= models.FileField(upload_to='projectoutput/',null=True,blank=True)
   split_pdf_location = models.CharField(max_length=255)  # For storing custom split PDF name
   split_date_time = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.original_pdf} - Part{self.split_date_time} -Part{self.split_pdf_location}"