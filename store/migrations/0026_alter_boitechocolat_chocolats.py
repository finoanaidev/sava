# Generated by Django 5.0.6 on 2024-07-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_alter_boitechocolat_chocolats_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boitechocolat',
            name='chocolats',
            field=models.ManyToManyField(default=0, related_name='boite_chocolats', to='store.chocolat'),
        ),
    ]
