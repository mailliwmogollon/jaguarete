# Generated by Django 3.2.4 on 2021-07-01 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TIENDAKAA', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='Categoria',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='Descripcion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='Precio',
            new_name='precio',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='Titulo',
            new_name='titulo',
        ),
    ]
