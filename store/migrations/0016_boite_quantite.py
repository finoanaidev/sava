# Generated by Django 5.0.6 on 2024-06-28 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_boite_chocolats'),
    ]

    operations = [
        migrations.AddField(
            model_name='boite',
            name='quantite',
            field=models.PositiveIntegerField(default=1),
        ),
    ]