# Generated by Django 3.2.25 on 2024-06-28 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfproject', '0003_alter_pdfsplitpart_split_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfsplitpart',
            name='split_file',
            field=models.CharField(max_length=200),
        ),
    ]
