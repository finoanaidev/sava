# Generated by Django 5.0.6 on 2024-07-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_boitechocolat_boite_chocolats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boitechocolat',
            name='quantite',
            field=models.PositiveIntegerField(default=0),
        ),
    ]