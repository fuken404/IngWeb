# Generated by Django 5.1.6 on 2025-02-12 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='imageurl',
        ),
        migrations.AddField(
            model_name='foto',
            name='imagen',
            field=models.ImageField(default='Thumbnail', upload_to='imagenes/'),
            preserve_default=False,
        ),
    ]
