# Generated by Django 3.2.25 on 2024-06-28 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdfproject', '0008_auto_20240628_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='splitpdf',
            name='original_pdf',
        ),
    ]
