# Generated by Django 5.1.1 on 2024-09-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_curso_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='imagen',
        ),
        migrations.AddField(
            model_name='curso',
            name='imagen_url',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
