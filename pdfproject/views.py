from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import PyPDF2
import os
from django.conf import settings

def front(request):
    return render(request, 'front.html')

def split_pdf(request):
    if request.method == 'POST' and request.FILES.get('file-input'):
        pdf_file = request.FILES['file-input']
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        output_dir = os.path.join(settings.MEDIA_ROOT, 'projectoutput')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        split_files = []
        for page_num in range(pdf_reader.numPages):
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_writer.addPage(pdf_reader.getPage(page_num))

            output_filename = os.path.join(output_dir, f'page_{page_num + 1}.pdf')
            with open(output_filename, 'wb') as output_file:
                pdf_writer.write(output_file)

            split_files.append(f'{settings.MEDIA_URL}projectouput/page_{page_num + 1}.pdf')

        response_data = {'files': split_files}
        return JsonResponse(response_data)

    #return JsonResponse({'error': 'Invalid request method or no file uploaded.'})

def view_split_files(request):
    output_dir = os.path.join(settings.MEDIA_ROOT, 'projectoutput')
    split_files = os.listdir(output_dir)
    return render(request, 'split_files.html', {'split_files': split_files})
