from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import PyPDF2
import os
from django.conf import settings
#from .forms import SplitPDF
from datetime import datetime
from .models import SplitPDF

def front(request):
    return render(request, 'template/front.html')

def split_pdf(request):
    if request.method == 'POST' and request.FILES['file-input']:
        pdf_file = request.FILES['file-input']
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        split_files = []
        input_file_name ,extension= os.path.splitext(pdf_file)
        output_dir = os.path.join(settings.MEDIA_ROOT,  input_file_name)
        os.makedirs(output_dir, exist_ok=True)
        split_pdf_instance = SplitPDF.objects.create(
                split_pdf_name = pdf_file,
                split_pdf_location = output_dir,
                split_date_time = datetime.now())
        split_pdf_instance.save()
   
        # Iterate over the range of total pages in the PDF document and add each page to the PdfWriter object
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_num])     
        
        # Construct the output file name and write the PDF content to the output file
            output_filename = os.path.join(output_dir, f'page_{page_num + 1}.pdf')
            with open(output_filename, 'wb') as output_file:
                    pdf_writer.write(output_file)
            
           # split_pdf_name = f'{pdf_file.name}_page_{page_num + 1}'
            #split_files.append(output_filename)
        #response_data = {'split_files': split_files}
        split_filess = os.listdir(output_dir)
        pdf_path = [request.build_absolute_uri(settings.MEDIA_URL + os.path.basename(files))for files in split_filess]

        return render(request, 'template/split_files.html', {'split_files': pdf_path})
    return render(request, 'template/split_files.html')
'''def upload_pdf(request):
    if request.method == 'POST':
        form =SplitPDF(request.POST, request.FILES)
        if form.is_valid():
            pdf = form.save()
            split_pdf = split_pdf(pdf)
        return render(request, 'template/upload', {'form': form})'''

    #return JsonResponse({'error': 'Invalid request method or no file uploaded.'})

'''def view_split_files(request):
    output_dir = os.path.join(settings.MEDIA_ROOT)
    
    split_files = os.listdir(output_dir)
    return render(request, 'template/split_files.html', {'split_files': split_files})'''
'''from django.shortcuts import render
from django.http import JsonResponse
import PyPDF2
import os
from django.conf import settings

def front(request):
    print("Rendering front page")  # Debugging statement
    return render(request, 'template/front.html')

def split_pdf(request):
    print("split_pdf view called")  # Debugging statement

    if request.method == 'POST' and request.FILES.get('file-input'):
        print("POST request and file upload detected")  # Debugging statement
        
        try:
            # Retrieve the uploaded PDF file from the request
            pdf_file = request.FILES['file-input']
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            print(f"PDF file read successfully, total pages: {pdf_reader.numPages}")  # Debugging statement

            # Specify the directory where the split PDF files will be stored
            output_dir = os.path.join(settings.MEDIA_ROOT, 'split_pdfs')
            os.makedirs(output_dir, exist_ok=True)
            print(f"Output directory created or already exists: {output_dir}")  # Debugging statement

            # Initialize an empty list to store the URLs of the split PDF files
            split_files = []
            for page_num in range(pdf_reader.numPages):
                print(f"Processing page {page_num + 1}")  # Debugging statement
                pdf_writer = PyPDF2.PdfFileWriter()
                pdf_writer.addPage(pdf_reader.getPage(page_num))

                # Specify the filename for the output PDF file
                output_filename = os.path.join(output_dir, f'page_{page_num + 1}.pdf')
                with open(output_filename, 'wb') as output_file:
                    pdf_writer.write(output_file)
                    print(f"Page {page_num + 1} written to {output_filename}")  # Debugging statement

                split_files.append(f'{settings.MEDIA_URL}split_pdfs/page_{page_num + 1}.pdf')
            print("All pages processed and written successfully")  # Debugging statement

            # Render the template with the list of split PDF files
            return render(request, 'template/split_files.html', {'split_files': split_files})
        
        except Exception as e:
            # Print the exception for debugging purposes
            print(f"An error occurred: {e}")
            return JsonResponse({'error': str(e)})
    
    # If the request method is not POST or no file is uploaded, return an error response
    print("Invalid request method or no file uploaded")  # Debugging statement
    return JsonResponse({'error': 'Invalid request method or no PDF file uploaded.'})

def view_split_files(request):
    print("view_split_files view called")  # Debugging statement
    output_dir = os.path.join(settings.MEDIA_ROOT, 'split_pdfs')
    split_files = os.listdir(output_dir)
    print(f"Split files found: {split_files}")  # Debugging statement
    return render(request, 'template/split_files.html', {'split_files': split_files})
'''