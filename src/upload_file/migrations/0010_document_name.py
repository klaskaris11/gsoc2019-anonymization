# Generated by Django 2.0.7 on 2019-07-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_file', '0009_auto_20190716_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default='default.txt', max_length=200),
        ),
    ]