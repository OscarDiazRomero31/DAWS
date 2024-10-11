# Generated by Django 5.1.1 on 2024-10-10 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_prestamos_cliente_libros'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='libros_preferidos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='favoritos', to='biblioteca.libro'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='libros',
            field=models.ManyToManyField(related_name='libros', through='biblioteca.Prestamos', to='biblioteca.libro'),
        ),
    ]