# Generated by Django 5.0.6 on 2024-06-05 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_products_other_description_products_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='video',
            field=models.FileField(upload_to='uploads/products/'),
        ),
    ]