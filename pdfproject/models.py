from django.db import models



# Create your models here.
class SplitPDF(models.Model):
    #original_pdf= models.FileField(verbose_name='pdf_split_parts/')
   split_pdf_name = models.CharField(max_length=255, )
   split_pdf_location = models.CharField(max_length=255)  # For storing custom split PDF name
   split_date_time = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.split_pdf_name} - Part{self.split_date_time} -Part{self.split_pdf_location}"