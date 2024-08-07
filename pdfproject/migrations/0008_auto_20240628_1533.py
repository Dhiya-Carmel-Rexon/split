# Generated by Django 3.2.25 on 2024-06-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfproject', '0007_alter_pdfsplitpart_split_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='SplitPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_pdf', models.FileField(upload_to='', verbose_name='pdf_split_parts/')),
                ('split_pdf_name', models.CharField(max_length=255, unique=True)),
                ('split_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='PDF',
        ),
        migrations.DeleteModel(
            name='PDFSplitPart',
        ),
    ]
