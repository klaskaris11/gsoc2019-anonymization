# Generated by Django 2.0.7 on 2019-07-23 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_file', '0014_document_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='anonymized_file_path',
            field=models.TextField(default=''),
        ),
    ]