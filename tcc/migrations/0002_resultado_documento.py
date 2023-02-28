# Generated by Django 4.1.7 on 2023-02-28 10:17

from django.db import migrations, models
import tcc.models.resultado


class Migration(migrations.Migration):

    dependencies = [
        ('tcc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultado',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to=tcc.models.resultado.get_file_path),
        ),
    ]
