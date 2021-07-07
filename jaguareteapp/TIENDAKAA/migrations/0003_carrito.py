# Generated by Django 3.2.4 on 2021-07-07 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TIENDAKAA', '0002_auto_20210701_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=250)),
                ('precio', models.CharField(max_length=2000)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
