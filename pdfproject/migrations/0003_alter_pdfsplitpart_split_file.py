# Generated by Django 3.2.25 on 2024-06-28 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfproject', '0002_auto_20240627_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfsplitpart',
            name='split_file',
            field=models.FileField(upload_to='', verbose_name='pdf_split_parts/'),
        ),
    ]