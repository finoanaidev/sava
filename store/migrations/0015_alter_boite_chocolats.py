# Generated by Django 5.0.6 on 2024-06-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_boite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boite',
            name='chocolats',
            field=models.ManyToManyField(blank=True, related_name='boites', to='store.chocolat'),
        ),
    ]