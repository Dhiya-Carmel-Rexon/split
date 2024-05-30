from django.shortcuts import render, redirect
from django.http import HttpResponse
import PyPDF2
import os

# Create your views here.
def front(request):
    return render(request, 'template/index.html')

def split(request):
    if request.method == 'GET' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Create a folder to save the split PDFs
        output_dir = 'splitted_pdfs'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Split the PDF
        for page_num in range(pdf_reader.numPages):
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_writer.addPage(pdf_reader.getPage(page_num))

            output_filename = f'{output_dir}/page_{page_num + 1}.pdf'
            with open(output_filename, 'wb') as output_file:
                pdf_writer.write(output_file)

        # Variable to pass to the template
        split_success_message = "PDF has been split successfully."

        return render(request, 'template/index.html', {'message': split_success_message})
    
    return redirect('index')




