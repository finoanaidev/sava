# Generated by Django 5.0.6 on 2024-06-28 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_boite_quantite'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoiteChocolat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nombre_chocolats', models.PositiveIntegerField()),
                ('boite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boite_chocolats', to='store.boite')),
                ('chocolats', models.ManyToManyField(related_name='boite_chocolats', to='store.chocolat')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boite_chocolats', to='store.customer')),
            ],
        ),
    ]